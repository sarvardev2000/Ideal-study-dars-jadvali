# -*- coding: utf-8 -*-
"""
IDEAL STUDY - Dars jadvali Telegram boti
==========================================
Bu botni ishga tushirish uchun:
  1) Terminalda shu papkaga kiring
  2) python -m venv venv          (bir marta)
  3) venv\\Scripts\\activate        (Windows)  yoki  source venv/bin/activate  (Mac/Linux)
  4) pip install -r requirements.txt
  5) .env faylini yarating va ichiga BOT_TOKEN=sizning_tokeningiz deb yozing
  6) python bot.py

Batafsil qo'llanma README.md faylida.
"""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

from schedule_data import CLASSES, TEACHERS, DAYS

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
router = Router()

# Sahifalardagi tugmalar sonini cheklash (o'qituvchilar ro'yxati uzun bo'lsa, sahifalarga bo'linadi)
PAGE_SIZE = 8

CLASS_NAMES = list(CLASSES.keys())
TEACHER_NAMES = sorted(TEACHERS.keys(), key=str.lower)


def get_grade(class_name: str) -> str:
    """'5-A' dan '5' ni ajratib oladi. Agar '-' bo'lmasa, sinf nomining o'zini qaytaradi."""
    return class_name.split("-")[0] if "-" in class_name else class_name


def all_grades() -> list:
    grades = []
    for name in CLASS_NAMES:
        g = get_grade(name)
        if g not in grades:
            grades.append(g)
    return grades


# ============================================================
# ASOSIY MENYU
# ============================================================

def main_menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="🏫 Sinflar bo'yicha", callback_data="menu_classes")
    kb.button(text="👨‍🏫 O'qituvchilar bo'yicha", callback_data="menu_teachers")
    kb.adjust(1)
    return kb.as_markup()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "👋 <b>IDEAL Study maktabining dars jadvaliga xush kelibsiz!</b>\n\n"
        "Quyidagi bo'limlardan birini tanlang:",
        reply_markup=main_menu_kb(),
    )


@router.callback_query(F.data == "main_menu")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "👋 <b>IDEAL Study maktabining dars jadvaliga xush kelibsiz!</b>\n\n"
        "Quyidagi bo'limlardan birini tanlang:",
        reply_markup=main_menu_kb(),
    )
    await callback.answer()


# ============================================================
# SINFLAR BO'LIMI:  parallel -> aniq sinf -> kun -> jadval
# ============================================================

@router.callback_query(F.data == "menu_classes")
async def show_grades(callback: CallbackQuery):
    kb = InlineKeyboardBuilder()
    for grade in all_grades():
        kb.button(text=f"{grade}-sinflar", callback_data=f"grade_{grade}")
    kb.button(text="⬅️ Orqaga", callback_data="main_menu")
    kb.adjust(2)
    await callback.message.edit_text("Qaysi parallel sinf kerak?", reply_markup=kb.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("grade_"))
async def show_classes_in_grade(callback: CallbackQuery):
    grade = callback.data.split("_", 1)[1]
    kb = InlineKeyboardBuilder()
    for idx, name in enumerate(CLASS_NAMES):
        if get_grade(name) == grade:
            kb.button(text=name, callback_data=f"cls_{idx}")
    kb.button(text="⬅️ Orqaga", callback_data="menu_classes")
    kb.adjust(3)
    await callback.message.edit_text(f"{grade}-sinflardan birini tanlang:", reply_markup=kb.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("cls_"))
async def show_class_days(callback: CallbackQuery):
    idx = int(callback.data.split("_", 1)[1])
    class_name = CLASS_NAMES[idx]
    kb = InlineKeyboardBuilder()
    for d_idx, day in enumerate(DAYS):
        kb.button(text=day, callback_data=f"clsday_{idx}_{d_idx}")
    kb.button(text="⬅️ Orqaga", callback_data=f"grade_{get_grade(class_name)}")
    kb.adjust(2)
    await callback.message.edit_text(f"📘 <b>{class_name}</b> sinfi. Qaysi kun kerak?", reply_markup=kb.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("clsday_"))
async def show_class_schedule(callback: CallbackQuery):
    _, idx, d_idx = callback.data.split("_")
    idx, d_idx = int(idx), int(d_idx)
    class_name = CLASS_NAMES[idx]
    day = DAYS[d_idx]
    lessons = CLASSES[class_name].get(day, [])

    if lessons:
        text = f"📘 <b>{class_name}</b> — {day}\n\n"
        for lesson in lessons:
            text += f"🕒 {lesson['soat']}\n📖 {lesson['fan']} — {lesson['ustoz']}\n\n"
    else:
        text = f"📘 <b>{class_name}</b> — {day}\n\nBu kuni dars yo'q."

    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Boshqa kun", callback_data=f"cls_{idx}")
    kb.button(text="🏠 Bosh menyu", callback_data="main_menu")
    kb.adjust(1)
    await callback.message.edit_text(text, reply_markup=kb.as_markup())
    await callback.answer()


# ============================================================
# O'QITUVCHILAR BO'LIMI:  sahifalangan ro'yxat -> kun -> jadval
# ============================================================

def teachers_page_kb(page: int):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    kb = InlineKeyboardBuilder()
    for idx, name in enumerate(TEACHER_NAMES[start:end], start=start):
        kb.button(text=name, callback_data=f"tch_{idx}")
    kb.adjust(1)

    nav = InlineKeyboardBuilder()
    if page > 0:
        nav.button(text="⬅️ Oldingi", callback_data=f"tchpage_{page - 1}")
    if end < len(TEACHER_NAMES):
        nav.button(text="Keyingi ➡️", callback_data=f"tchpage_{page + 1}")
    nav.adjust(2)

    kb.attach(nav)
    back = InlineKeyboardBuilder()
    back.button(text="⬅️ Bosh menyu", callback_data="main_menu")
    kb.attach(back)
    return kb.as_markup()


@router.callback_query(F.data == "menu_teachers")
async def show_teachers_page0(callback: CallbackQuery):
    await callback.message.edit_text("O'qituvchini tanlang:", reply_markup=teachers_page_kb(0))
    await callback.answer()


@router.callback_query(F.data.startswith("tchpage_"))
async def show_teachers_page(callback: CallbackQuery):
    page = int(callback.data.split("_", 1)[1])
    await callback.message.edit_text("O'qituvchini tanlang:", reply_markup=teachers_page_kb(page))
    await callback.answer()


@router.callback_query(F.data.startswith("tch_"))
async def show_teacher_days(callback: CallbackQuery):
    idx = int(callback.data.split("_", 1)[1])
    teacher_name = TEACHER_NAMES[idx]
    kb = InlineKeyboardBuilder()
    for d_idx, day in enumerate(DAYS):
        kb.button(text=day, callback_data=f"tchday_{idx}_{d_idx}")
    kb.button(text="⬅️ Orqaga", callback_data="menu_teachers")
    kb.adjust(2)
    await callback.message.edit_text(f"👤 <b>{teacher_name}</b>. Qaysi kun kerak?", reply_markup=kb.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("tchday_"))
async def show_teacher_schedule(callback: CallbackQuery):
    _, idx, d_idx = callback.data.split("_")
    idx, d_idx = int(idx), int(d_idx)
    teacher_name = TEACHER_NAMES[idx]
    day = DAYS[d_idx]
    lessons = TEACHERS[teacher_name].get(day, [])

    if lessons:
        text = f"👤 <b>{teacher_name}</b> — {day}\n\n"
        for lesson in lessons:
            text += f"🕒 {lesson['soat']}\n🏫 {lesson['sinf']} — {lesson['fan']}\n\n"
        text += f"Jami: {len(lessons)} soat dars."
    else:
        text = f"👤 <b>{teacher_name}</b> — {day}\n\nBu kuni dars yo'q."

    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Boshqa kun", callback_data=f"tch_{idx}")
    kb.button(text="🏠 Bosh menyu", callback_data="main_menu")
    kb.adjust(1)
    await callback.message.edit_text(text, reply_markup=kb.as_markup())
    await callback.answer()


# ============================================================
# ERKIN YOZILGAN XABARLARGA JAVOB (tugmalardan foydalanish kerak)
# ============================================================

@router.message()
async def any_text(message: Message):
    await message.answer(
        "Iltimos, faqat tugmalardan foydalaning 🙂",
        reply_markup=main_menu_kb(),
    )


async def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN topilmadi! .env faylini yarating va ichiga "
            "BOT_TOKEN=sizning_tokeningiz deb yozing (README.md ga qarang)."
        )
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

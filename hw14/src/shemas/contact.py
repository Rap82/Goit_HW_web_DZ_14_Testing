from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr

# from src.database.models import User
from src.shemas.users import UserResponse


class ContactModel(BaseModel):
    first_name: str = Field(
        default="",
        examples=["Михайло", "Остап"],
        min_length=3,
        max_length=25,
        title="Ім'я",
    )
    last_name: str = Field(
        default="",
        examples=["Грушевський", "Вишня"],
        min_length=3,
        max_length=25,
        title="Прізвище",
    )
    email: EmailStr
    phone: str | None = Field(
        None,
        examples=["+380 44 123-4567", "+380 (44) 1234567", "+380441234567"],
        max_length=25,
        title="Номер телефону",
    )
    birthday: date | None = None
    comments: str | None = Field(default=None, title="Додаткові дані")
    favorite: bool = False
    # user_id: int = Field(1, gt=0)


class ContactFavoriteModel(BaseModel):
    favorite: bool = False

    # pattern=r"^+[0-9\s\(\)-]+$


class ContactResponse(BaseModel):
    id: int
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
    phone: str | None
    birthday: date | None
    comments: str | None
    favorite: bool
    created_at: datetime
    updated_at: datetime
    user: UserResponse

    class Config:
        from_attributes = True
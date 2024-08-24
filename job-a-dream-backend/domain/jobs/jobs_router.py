from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.corporations import corp_crud, corp_schemas
from typing import List

router = APIRouter()

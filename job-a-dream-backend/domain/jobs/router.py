from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connector import get_db
from domain.jobs import crud, schemas
from typing import List

router = APIRouter()

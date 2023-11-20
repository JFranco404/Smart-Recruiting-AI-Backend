from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Main"])
def main():
    return {"message": "Hello World"}

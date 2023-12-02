from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Principal"])
def main():
    return {"message": "Hello World"}

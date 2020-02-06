from typing import Dict

from fastapi import FastAPI

app = FastAPI(title='Burriking API')


@app.get('/_health', status_code=200)
def get_check() -> Dict:
    return dict(status='OK')

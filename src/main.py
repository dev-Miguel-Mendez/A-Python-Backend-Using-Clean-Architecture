

import uvicorn
from bootstrap_env import load_env
from interfaces.db.emit_base import emit_base



if __name__ == "__main__":


    load_env()
    
    emit_base()
    
    uvicorn.run(
        app="interfaces.http.app:app",
        port=3001,
        reload=True,
    )
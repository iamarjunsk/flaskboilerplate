from app import app

mode = 'dev'
if mode == 'dev':
    app.debug = True
else:
    app.debug = False

if __name__ == "__main__":
    app.run()

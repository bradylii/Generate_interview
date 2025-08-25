# Generate_interview
Track 1: ngrok challenge

Because I am using the free plan, my ngrock link might change so here are the instructions:

Start the server with:
uvicorn main:app --reload

Expose it to the internet with:
ngrok http 8000

Test Server:
curl http://127.0.0.1:8000/healthcheck

or via ngrok:
curl https://<your-ngrok-link>/healthcheck

Thank your time and consideration! :D 

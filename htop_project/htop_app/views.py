from django.http import HttpResponse
import os
import subprocess
import datetime

def htop_view(request):
    name = "Chetan S"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -b -n 1")  # Run 'top' command in batch mode

    response = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time: {server_time}</h2>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)

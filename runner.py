import subprocess, time, psutil, os

def run_code(file_path, lang):
    start_time = time.time()
    process = None

    
    if lang == "python":
        process = subprocess.Popen(["python", file_path], stdout=subprocess.PIPE)
    elif lang == "cpp":
        exe_file = file_path.replace(".cpp", "")
        subprocess.run(["g++", file_path, "-o", exe_file])
        process = subprocess.Popen([f"./{exe_file}"], stdout=subprocess.PIPE)
    elif lang == "go":
        process = subprocess.Popen(["go", "run", file_path], stdout=subprocess.PIPE)
    else:
        raise ValueError(f"Unsupported language: {lang}")

    pid = process.pid
    p = psutil.Process(pid)
    mem_usage = 0


    while process.poll() is None:
        try:
            mem_usage = max(mem_usage, p.memory_info().rss / 1024 / 1024)
        except psutil.NoSuchProcess:
            break

    exec_time = time.time() - start_time
    return exec_time, mem_usage

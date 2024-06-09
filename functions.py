def counter():
    for i in range(100):
        time.sleep(0.1)
        print(str(i))
        progress_bar['value'] = i+1
    # progress_bar.stop()

def download_file():
    label1["text"] = "Analyzing..."
    # Disable the button while downloading the file.
    button1["state"] = "disabled"
    # Start the download in a new thread.
    t = threading.Thread(target=counter)
    t.start()
    # Start checking periodically if the thread has finished.
    schedule_check(t)


def check_if_done(t):
    # If the thread has finished, re-enable the button and show a message.
    if not t.is_alive():
        label1["text"] = "File successfully analyzed!"
        button1["state"] = "normal"
    else:
        # Otherwise check again after one second.
        schedule_check(t)

def schedule_check(t):
    """
    Schedule the execution of the `check_if_done()` function after
    one second.
    """
    root.after(1000, check_if_done, t)

def end_program():
    exit()
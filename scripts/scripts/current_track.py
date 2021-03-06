import subprocess


def main():
    st = subprocess.getoutput("mpc")
    lin = st.split("\n")
    if len(lin) > 1:
        sn_status = lin[1]
        duration = lin[1].split()
        if "paused" in sn_status:
            print(lin[0].split("-")[-1] + " [paused]")
        elif "playing" in sn_status:
            print(lin[0].split("-")[-1] + "   " + duration[2])
        else:
            print("stopped")
    else:
        print("stopped")


if __name__ == "__main__":
    main()

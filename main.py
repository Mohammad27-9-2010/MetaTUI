# main.py
import curses
from msf_helper import MetasploitHelper

def main(stdscr):
    msf = MetasploitHelper()
    curses.curs_set(0)
    stdscr.clear()
    
    # Instructions
    stdscr.addstr(0, 0, "Metasploit TUI - Type 'q' to exit")
    stdscr.addstr(1, 0, "Press 'e' to list exploits, 'c' to execute a command")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        
        if key == ord('q'):
            break  # Exit the program
        elif key == ord('e'):
            show_exploits(stdscr, msf)
        elif key == ord('c'):
            execute_command(stdscr, msf)

def show_exploits(stdscr, msf):
    stdscr.clear()
    stdscr.addstr(0, 0, "Available Exploits:")
    exploits = msf.get_exploits()
    for idx, exploit in enumerate(exploits, start=1):
        stdscr.addstr(idx, 0, exploit)
    stdscr.addstr(len(exploits) + 1, 0, "Press any key to return")
    stdscr.getch()

def execute_command(stdscr, msf):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter Metasploit command:")
    command = stdscr.getstr(1, 0).decode('utf-8')
    result = msf.execute_command(command)
    stdscr.clear()
    stdscr.addstr(0, 0, f"Command Result: {result}")
    stdscr.addstr(2, 0, "Press any key to return")
    stdscr.getch()
    curses.noecho()

if __name__ == "__main__":
    curses.wrapper(main)

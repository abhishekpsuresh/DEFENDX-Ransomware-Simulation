#!/usr/bin/env python3
"""
DEFENDX - Dummy Ransomware Simulation
Educational Purpose Only - No Real Encryption
TASK 2 (40 Marks)
"""

import tkinter as tk
from tkinter import messagebox
import sys

# ========== CONFIGURATION ==========
CORRECT_PASSWORD = "defendx123"  # Password to unlock
# ===================================

class RansomwareSim:
    def __init__(self):
        # Create main window
        self.window = tk.Tk()
        self.window.title("⚠️ SYSTEM LOCKED ⚠️")
        
        # Get screen dimensions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        # Set window to full screen
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg='black')
        
        # Prevent closing with Alt+F4 or X button
        self.window.protocol("WM_DELETE_WINDOW", self.block_close)
        
        # Create main frame
        self.main_frame = tk.Frame(self.window, bg='black')
        self.main_frame.pack(expand=True, fill='both')
        
        # Skull/Block icon
        self.skull_label = tk.Label(
            self.main_frame,
            text="💀 🔒 💀",
            font=("Arial", 100),
            fg="red",
            bg="black"
        )
        self.skull_label.pack(pady=50)
        
        # Warning title
        self.title_label = tk.Label(
            self.main_frame,
            text="YOUR SYSTEM HAS BEEN LOCKED!",
            font=("Arial", 44, "bold"),
            fg="red",
            bg="black"
        )
        self.title_label.pack(pady=20)
        
        # Informational message
        self.message_label = tk.Label(
            self.main_frame,
            text="⚠️ This is a SAFE SIMULATION for educational purposes only ⚠️\n\n"
                 "No files have been encrypted or damaged.\n"
                 "Real ransomware would demand payment to unlock your files.\n\n"
                 "Enter the correct password to unlock your system.",
            font=("Arial", 14),
            fg="white",
            bg="black",
            justify="center"
        )
        self.message_label.pack(pady=30)
        
        # Password label
        self.pass_label = tk.Label(
            self.main_frame,
            text="🔐 ENTER PASSWORD TO UNLOCK:",
            font=("Arial", 20, "bold"),
            fg="yellow",
            bg="black"
        )
        self.pass_label.pack(pady=15)
        
        # Password entry field
        self.password_entry = tk.Entry(
            self.main_frame,
            font=("Arial", 22),
            width=25,
            show="*",
            bg="gray20",
            fg="white",
            insertbackground="white",
            justify="center"
        )
        self.password_entry.pack(pady=10)
        self.password_entry.bind('<Return>', self.check_password)
        self.password_entry.focus()
        
        # Unlock button
        self.unlock_btn = tk.Button(
            self.main_frame,
            text="🔓 UNLOCK SYSTEM 🔓",
            font=("Arial", 16, "bold"),
            bg="red",
            fg="white",
            activebackground="darkred",
            activeforeground="white",
            cursor="hand2",
            command=self.check_password_wrapper
        )
        self.unlock_btn.pack(pady=20)
        
        # Attempt counter
        self.attempts = 0
        self.attempt_label = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 12),
            fg="gray",
            bg="black"
        )
        self.attempt_label.pack(pady=10)
        
        # Start the application
        self.window.mainloop()
    
    def block_close(self):
        """Block window close attempts - prevents bypass"""
        pass
    
    def check_password_wrapper(self):
        """Wrapper for button click"""
        self.check_password(None)
    
    def check_password(self, event):
        """Verify password and unlock system"""
        password = self.password_entry.get()
        self.attempts += 1
        
        if password == CORRECT_PASSWORD:
            # Correct password - success!
            messagebox.showinfo(
                "✅ SYSTEM UNLOCKED ✅",
                f"System Unlocked Successfully!\n\n"
                f"Attempts used: {self.attempts}\n\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                f"⚠️ EDUCATIONAL SIMULATION ⚠️\n"
                f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"No files were encrypted or damaged.\n"
                f"This was a safe simulation.\n\n"
                f"Real ransomware would:\n"
                f"• Encrypt all your documents\n"
                f"• Demand Bitcoin payment\n"
                f"• Threaten permanent data loss"
            )
            self.window.destroy()
            sys.exit(0)
        else:
            # Wrong password - show error
            remaining = 3 - (self.attempts % 3) if (self.attempts % 3) != 0 else 3
            self.attempt_label.config(
                text=f"❌ INCORRECT PASSWORD! (Attempt {self.attempts})",
                fg="red"
            )
            self.password_entry.delete(0, tk.END)
            self.password_entry.config(bg="darkred")
            self.window.after(300, lambda: self.password_entry.config(bg="gray20"))
            self.password_entry.focus()

# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    print("="*60)
    print("  DEFENDX - Ransomware Simulation (TASK 2)")
    print("  Educational Purpose Only")
    print("="*60)
    print(f"  🔐 Password for testing: {CORRECT_PASSWORD}")
    print("  🚪 Press 'Esc' to exit if needed")
    print("="*60)
    print("  Starting simulation...")
    print("="*60)
    
    RansomwareSim()

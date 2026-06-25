import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from main import detect_wifi_networks, visualize_signal_strength, visualize_heatmap


class WiFiAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WiFi Analyzer")
        self.root.geometry("1000x700")
        self.networks = []

        # Apply Modern Theme
        self.style = Style("darkly")  # Choose theme: darkly, cosmo, minty, etc.
        self.root.configure(bg=self.style.colors.bg)

        # Frames
        self.top_frame = ttk.Frame(self.root, padding="10")
        self.top_frame.pack(fill=tk.X)

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.details_frame = ttk.Frame(self.root, padding="10", width=300)
        self.details_frame.pack(fill=tk.BOTH, expand=False, side=tk.RIGHT)

        # Search Bar
        self.search_var = tk.StringVar()
        self.search_bar = ttk.Entry(
            self.top_frame,
            textvariable=self.search_var,
            font=("Helvetica", 12),
            width=40,
        )
        self.search_bar.pack(side=tk.LEFT, padx=10, pady=5)
        self.search_bar.insert(0, "Search by SSID...")
        self.search_bar.bind("<KeyRelease>", self.filter_networks)

        # Buttons with Icons
        self.refresh_button = ttk.Button(
            self.top_frame, text="🔄 Refresh Networks", command=self.refresh_networks, style="success.TButton"
        )
        self.refresh_button.pack(side=tk.LEFT, padx=5)

        self.graph_button = ttk.Button(
            self.top_frame,
            text="📊 View Graph",
            command=self.show_graph,
            style="info.TButton",
        )
        self.graph_button.pack(side=tk.LEFT, padx=5)

        self.heatmap_button = ttk.Button(
            self.top_frame,
            text="🌐 View Heatmap",
            command=self.show_heatmap,
            style="primary.TButton",
        )
        self.heatmap_button.pack(side=tk.LEFT, padx=5)

        self.dark_mode_toggle = ttk.Button(
            self.top_frame,
            text="🌙 Toggle Dark Mode",
            command=self.toggle_dark_mode,
            style="warning.TButton",
        )
        self.dark_mode_toggle.pack(side=tk.RIGHT, padx=10)

        # Treeview for displaying networks
        self.tree = ttk.Treeview(
            self.main_frame,
            columns=("SSID", "Signal Strength", "Channel"),
            show="headings",
        )
        self.tree.heading("SSID", text="SSID")
        self.tree.heading("Signal Strength", text="Signal Strength (%)")
        self.tree.heading("Channel", text="Channel")
        self.tree.column("SSID", width=300)
        self.tree.column("Signal Strength", width=150, anchor=CENTER)
        self.tree.column("Channel", width=100, anchor=CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.show_details)

        # Details Frame
        ttk.Label(self.details_frame, text="Network Details", font=("Helvetica", 16)).pack(
            anchor=tk.NW, pady=10
        )
        self.details_text = tk.Text(
            self.details_frame,
            wrap=tk.WORD,
            font=("Courier New", 12),
            state=tk.DISABLED,
            height=20,
            bg=self.style.colors.bg,
            fg=self.style.colors.light,
        )
        self.details_text.pack(fill=tk.BOTH, expand=True)

        # Initial Load
        self.refresh_networks()

    def refresh_networks(self):
        """Refresh the list of networks and update the Treeview."""
        try:
            self.networks = detect_wifi_networks()

            # Clear the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert new data into the Treeview
            for network in self.networks:
                self.tree.insert(
                    "", tk.END,
                    values=(
                        network["SSID"],
                        f"{network['Signal Strength']}%",
                        network["Channel"],
                    ),
                )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh networks: {e}")

    def filter_networks(self, event=None):
        """Filter the networks in the Treeview based on SSID."""
        query = self.search_var.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)

        filtered_networks = [
            net
            for net in self.networks
            if query in net["SSID"].lower()
        ]
        for network in filtered_networks:
            self.tree.insert(
                "", tk.END,
                values=(
                    network["SSID"],
                    f"{network['Signal Strength']}%",
                    network["Channel"],
                ),
            )

    def show_details(self, event=None):
        """Display detailed information about the selected network."""
        selected = self.tree.focus()
        if not selected:
            return

        values = self.tree.item(selected, "values")
        selected_ssid = values[0]

        # Find the network details
        for network in self.networks:
            if network["SSID"] == selected_ssid:
                details = "\n".join(
                    [f"{key}: {value}" for key, value in network.items()]
                )
                self.details_text.configure(state=tk.NORMAL)
                self.details_text.delete("1.0", tk.END)
                self.details_text.insert(tk.END, details)
                self.details_text.configure(state=tk.DISABLED)
                return

    def show_graph(self):
        """Display a bar chart of WiFi signal strength."""
        if not self.networks:
            messagebox.showwarning("No Networks", "No networks available to visualize.")
            return
        visualize_signal_strength(self.networks)

    def show_heatmap(self):
        """Display a heatmap of WiFi signal strength."""
        if not self.networks:
            messagebox.showwarning("No Networks", "No networks available to visualize.")
            return
        visualize_heatmap(self.networks)

    def toggle_dark_mode(self):
        """Toggle between light and dark mode themes."""
        current_theme = self.style.theme_use()
        if current_theme == "darkly":
            self.style.theme_use("cosmo")  # Light theme
        else:
            self.style.theme_use("darkly")  # Dark theme


if __name__ == "__main__":
    root = tk.Tk()
    app = WiFiAnalyzerGUI(root)
    root.mainloop()

# Released under the MIT License. See LICENSE for details.

"""Admin module for managing server administrators."""

from typing import List

class AdminManager:
    """Class to manage server administrators."""

    def __init__(self):
        self.admins: List[str] = []

    def add_admin(self, admin_id: str) -> None:
        """Add a new admin by their ID."""
        if admin_id not in self.admins:
            self.admins.append(admin_id)

    def remove_admin(self, admin_id: str) -> None:
        """Remove an admin by their ID."""
        if admin_id in self.admins:
            self.admins.remove(admin_id)

    def is_admin(self, admin_id: str) -> bool:
        """Check if a given ID belongs to an admin."""
        return admin_id in self.admins

    def get_admins(self) -> List[str]:
        """Get the list of all admin IDs."""
        return self.admins

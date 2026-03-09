class RideSharing:
    """A simple ride-sharing class."""

    def __init__(self):
        self.rides = []

    def request_ride(self, user):
        """Request a ride for the user."""
        self.rides.append(user)
        return f"Ride requested for {user}"

# Example usage
if __name__ == '__main__':
    service = RideSharing()
    print(service.request_ride('John Doe'))

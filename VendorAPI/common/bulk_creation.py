from VendorAPI.models import *

# Status Table
def StatusCreation():
    Status.objects.bulk_create(
        [
            Status(
                statusid=1,
                status_name="Pending",
                status_color="warning",
            ),
            Status(
                statusid=2,
                status_name="Completed",
                status_color="success",
            ),
            Status(
                statusid=3,
                status_name="Canceled",
                status_color="danger",
            ),
            
        ]
    )


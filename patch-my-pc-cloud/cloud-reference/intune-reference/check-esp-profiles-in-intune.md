# Check ESP Profiles in Intune

_Applies to: Microsoft Intune_

If a Patch My PC (PMPC) Cloud deployment has been configured to use [ESP Profiles](../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/esp-profiles-deployments.md), this is how you can check the deployment(s) has been added to the correct ESP Profile in Intune:

1. Sign in to the <strong>Intune admin center</strong>
2.  Navigate to <strong>Devices</strong>\


    ![Navigating to “Devices”](/_images/image-(126).png "Navigating to “Devices”")
3.  Navigate to <strong>Enrollment</strong>\


    ![Navigating to “Enrollment”](/_images/image-(276).png "Navigating to “Enrollment”")


4.  Scroll down and select <strong>Enrollment Status Page</strong>\


    ![Scrolling down and selecting “Enrollment Status Page”](/_images/image-(277).png "Scrolling down and selecting “Enrollment Status Page”")


5.  On the <strong>Enrollment Status Page</strong> click the relevant profile the PMPC Cloud deployment has been added to.\


    ![Clicking the relevant profile the PMPC Cloud deployment has been added to](/_images/image-(278).png "Clicking the relevant profile the PMPC Cloud deployment has been added to")


6.  On the _<strong>\<profile\_name></strong>_ page, navigate to <strong>Manage | Properties</strong>\


    ![Navigating to “Manage | Properties”](/_images/image-(279).png "Navigating to “Manage | Properties”")


7.  Scroll down to the <strong>Block device use until required apps are installed if they are assigned to the user/device</strong> field. This shows the apps that must be installed before the user can use the device and will include the PMPC Cloud deployment if it was configured correctly.\


    ![Scrolling down to the “Block device use until required apps are installed if they are assigned to the user/device field”, which shows the apps that must be installed before a user can use the device](/_images/image-(280).png "Scrolling down to the “Block device use until required apps are installed if they are assigned to the user/device field”, which shows the apps that must be installed before a user can use the device")
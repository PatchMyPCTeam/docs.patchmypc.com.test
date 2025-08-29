# Check ESP Profiles in Intune

_Applies to: Microsoft Intune_

If a Patch My PC (PMPC) Cloud deployment has been configured to use [ESP Profiles](../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/esp-profiles-deployments.md), this is how you can check the deployment(s) has been added to the correct ESP Profile in Intune:

1. Sign in to the **Intune admin center**
2.  Navigate to **Devices**\


    <figure><img src="../../../.gitbook/assets/image (126).png" alt="Navigating to “Devices”"><figcaption></figcaption></figure>
3.  Navigate to **Enrollment**\


    <figure><img src="../../../.gitbook/assets/image (276).png" alt="Navigating to “Enrollment”"><figcaption></figcaption></figure>


4.  Scroll down and select **Enrollment Status Page**\


    <figure><img src="../../../.gitbook/assets/image (277).png" alt="Scrolling down and selecting “Enrollment Status Page”"><figcaption></figcaption></figure>


5.  On the **Enrollment Status Page** click the relevant profile the PMPC Cloud deployment has been added to.\


    <figure><img src="../../../.gitbook/assets/image (278).png" alt="Clicking the relevant profile the PMPC Cloud deployment has been added to"><figcaption></figcaption></figure>


6.  On the _**\<profile\_name>**_ page, navigate to **Manage | Properties**\


    <figure><img src="../../../.gitbook/assets/image (279).png" alt="Navigating to “Manage | Properties”"><figcaption></figcaption></figure>


7.  Scroll down to the **Block device use until required apps are installed if they are assigned to the user/device** field. This shows the apps that must be installed before the user can use the device and will include the PMPC Cloud deployment if it was configured correctly.\


    <figure><img src="../../../.gitbook/assets/image (280).png" alt="Scrolling down to the “Block device use until required apps are installed if they are assigned to the user/device field”, which shows the apps that must be installed before a user can use the device"><figcaption></figcaption></figure>

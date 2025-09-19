# Check ESP Profiles in Intune

_Applies to: Microsoft Intune_

If a Patch My PC (PMPC) Cloud deployment has been configured to use [ESP Profiles](../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/esp-profiles-deployments.md), this is how you can check the deployment(s) has been added to the correct ESP Profile in Intune:

1. Sign in to the **Intune admin center**
2.  Navigate to **Devices**\\

    ![Navigating to “Devices”](../../../.gitbook/assets/image-\(126\).png)
3.  Navigate to **Enrollment**\\

    ![Navigating to “Enrollment”](../../../.gitbook/assets/image-\(276\).png)
4.  Scroll down and select **Enrollment Status Page**\\

    ![Scrolling down and selecting “Enrollment Status Page”](../../../.gitbook/assets/image-\(277\).png)
5.  On the **Enrollment Status Page** click the relevant profile the PMPC Cloud deployment has been added to.\\

    ![Clicking the relevant profile the PMPC Cloud deployment has been added to](../../../.gitbook/assets/image-\(278\).png)
6.  On the _**\<profile\_name>**_ page, navigate to **Manage | Properties**\\

    ![Navigating to “Manage | Properties”](../../../.gitbook/assets/image-\(279\).png)
7.  Scroll down to the **Block device use until required apps are installed if they are assigned to the user/device** field. This shows the apps that must be installed before the user can use the device and will include the PMPC Cloud deployment if it was configured correctly.\\

    ![Scrolling down to the “Block device use until required apps are installed if they are assigned to the user/device field”, which shows the apps that must be installed before a user can use the device](../../../.gitbook/assets/image-\(280\).png)

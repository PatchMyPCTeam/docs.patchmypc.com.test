# Check ESP Profiles in Intune

_Applies to: Microsoft Intune_

If a Patch My PC (PMPC) Cloud deployment has been configured to use [ESP Profiles](../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/esp-profiles-deployments.md), this is how you can check the deployment(s) has been added to the correct ESP Profile in Intune:

1. Sign in to the **Intune admin center**
2.  Navigate to **Devices**\


    ![Navigating to “Devices”](../../../_images/image%20%28126%29.png%20"Navigating%20to%20\"Devices\"")
3.  Navigate to **Enrollment**\


    ![Navigating to “Enrollment”](../../../_images/image%20%28276%29.png%20"Navigating%20to%20\"Enrollment\"")


4.  Scroll down and select **Enrollment Status Page**\


    ![Scrolling down and selecting “Enrollment Status Page”](../../../_images/image%20%28277%29.png%20"Scrolling%20down%20and%20selecting%20\"Enrollment%20Status%20Page\"")


5.  On the **Enrollment Status Page** click the relevant profile the PMPC Cloud deployment has been added to.\


    ![Clicking the relevant profile the PMPC Cloud deployment has been added to](../../../_images/image%20%28278%29.png%20"Clicking%20the%20relevant%20profile%20the%20PMPC%20Cloud%20deployment%20has%20been%20added%20to")


6.  On the _**\<profile\_name>**_ page, navigate to **Manage | Properties**\


    ![Navigating to “Manage | Properties”](../../../_images/image%20%28279%29.png%20"Navigating%20to%20\"Manage%20|%20Properties\"")


7.  Scroll down to the **Block device use until required apps are installed if they are assigned to the user/device** field. This shows the apps that must be installed before the user can use the device and will include the PMPC Cloud deployment if it was configured correctly.\


    ![Scrolling down to the “Block device use until required apps are installed if they are assigned to the user/device field”, which shows the apps that must be installed before a user can use the device](../../../_images/image%20%28280%29.png%20"Scrolling%20down%20to%20the%20\"Block%20device%20use%20until%20required%20apps%20are%20installed%20if%20they%20are%20assigned%20to%20the%20user/device%20field\",%20which%20shows%20the%20apps%20that%20must%20be%20installed%20before%20a%20user%20can%20use%20the%20device")

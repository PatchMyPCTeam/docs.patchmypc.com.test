# Why is the “Deploy” button greyed out in Cloud?

_Applies to: Patch My PC Cloud_

### SYMPTOMS

Why when I try to deploy an app, is the **Deploy** button greyed out?

![“Deploy” button greyed out.](../../../_images/image%20%282342%29.png%20"\"Deploy\"%20button%20greyed%20out.")

### CAUSE

This can be caused if you add the **UpdateOnly** assignment type to a deployment that is configured to use an [ESP Profile](../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/esp-profiles-deployments.md) which is unsupported in Intune. If you look at the **Configurations** tab it will show a read "**X**" highlighting the configuration conflict.

### RESOLUTION

To resolve this issue:

1.  Click the **Configurations** page of the deployment.\


    ![Clicking the “Configurations” page](../../../_images/image%20%282375%29.png%20"Clicking%20the%20\"Configurations\"%20page")

    \
    If the problem is caused by an ESP Profile being configured, the **ESP Profiles** tab will be automatically opened.\


    ![“ESP Profile” tab automatically opened](../../../_images/image%20%282344%29.png%20"\"ESP%20Profile\"%20tab%20automatically%20opened")


2.  Scroll down to the **ESP Profiles** section, under which you will see the following message:\


    **ESP profiles should be empty when the assignments list contains only UpdateOnly assignments.**\


    ![“ESP profiles should be empty when the assignments list contains only UpdateOnly assignments.” message](../../../_images/image%20%282345%29.png%20"\"ESP%20profiles%20should%20be%20empty%20when%20the%20assignments%20list%20contains%20only%20UpdateOnly%20assignments.\"%20message")


3.  You now need to decide whether you:

    a. Remove the **UpdateOnly** assignment

    b. Change this deployment to not use any ESP Profiles.\
    \
    Either of these options will enable the **Deploy** button.

# Why is the “Deploy” button greyed out in Cloud?

_Applies to: Patch My PC Cloud_

### SYMPTOMS

Why when I try to deploy an app, is the **Deploy** button greyed out?

!["Deploy" button greyed out.](/_images/image-(2342 '"Deploy" button greyed out.').png "“Deploy” button greyed out.")

### CAUSE

This can be caused if you add the **UpdateOnly** assignment type to a deployment that is configured to use an [ESP Profile](../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/esp-profiles-deployments.md) which is unsupported in Intune. If you look at the **Configurations** tab it will show a read "**X**" highlighting the configuration conflict.

### RESOLUTION

To resolve this issue:

1.  Click the **Configurations** page of the deployment.\


    ![Clicking the "Configurations" page](/_images/image-(2375 'Clicking the "Configurations" page').png "Clicking the “Configurations” page")

    \
    If the problem is caused by an ESP Profile being configured, the **ESP Profiles** tab will be automatically opened.\


    !["ESP Profile" tab automatically opened](/_images/image-(2344 '"ESP Profile" tab automatically opened').png "“ESP Profile” tab automatically opened")


2.  Scroll down to the **ESP Profiles** section, under which you will see the following message:\


    **ESP profiles should be empty when the assignments list contains only UpdateOnly assignments.**\


    !["ESP profiles should be empty when the assignments list contains only UpdateOnly assignments." message](/_images/image-(2345 '"ESP profiles should be empty when the assignments list contains only UpdateOnly assignments." message').png "“ESP profiles should be empty when the assignments list contains only UpdateOnly assignments.” message")


3.  You now need to decide whether you:

    a. Remove the **UpdateOnly** assignment

    b. Change this deployment to not use any ESP Profiles.\
    \
    Either of these options will enable the **Deploy** button.
---
description: Details how to connect the Patch My PC Publisher to our Cloud platform
hidden: true
---

# Integrate Publisher

_Applies to: Custom Apps_

If you plan to use our on-premises Publisher to publish your Custom Apps, you need to integrate it as detailed below before you can create a Custom App.

> **Note**
>
> If you only plan to use Intune Apps for Cloud to deploy your Custom Apps, you do not need to complete this process and can now \[Create a Custom App]\(create-a-custom-app/).

To connect Publisher to PMPC Cloud:

1. Load the **Patch My PC Publishing Service** (Publisher) and verify you are running at least version 2.1.20.0. If you are not, upgrade to the latest version.
2. Click the **Cloud** tab.

> Tip
>
> If the **Cloud** tab is not present, check you have entered your license key and clicked **Validate**.

!["Cloud" tab of our Publisher](/_images/image-(1725 "\"Cloud\" tab of our Publisher").png)

3. In the **Connection Name** field, enter a unique name for the connection. For example **Patch My PC Custom Apps**, then click **Connect**.

> **Note**
>
> The name you enter here determines how this connection shows on the **Connections** page of the **portal**.

![Entering a "Connection Name" and clicking "Connect"](/_images/image-(1726 "Entering a \"Connection Name\" and clicking \"Connect\"").png)

4.  In your browser, enter the Entra ID you used to onboard to PMPC Cloud or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.

    !["Microsoft Sign in" screen](/_images/image-(1420 "\"Microsoft Sign in\" screen").png)
5.  Enter the password and click **Sign in**.

    !["Enter password" screen](/_images/image-(1421 "\"Enter password\" screen").png)

    \
    If the connection is successful, a new browser tab opens with the following message:

    **Authentication complete. You can return to the application. Feel free to close this browser tab.**\
    \
    You can close this tab at this point.\\
6. If the **Edit a customer** screen is not displayed, proceed to Step 8.
7.  If the **Edit a customer** screen is displayed, click to select the customer you want to connect to, then click **OK**.\\

    ![Selecting the relevant customer from the "Edit a customer" screen](/_images/image-(910 "Selecting the relevant customer from the \"Edit a customer\" screen").png)
8.  In Publisher, verify the **Connection Status** shows as **Connected**, then click **Save and Close**.\\

    ![Publisher showing it's "Connected"](/_images/image-(1728 "Publisher showing it's \"Connected\"").png)

> **Note**
>
> You can also use the \[Verifying the Publisher connection from the Portal]\(../cloud-administration/manage-cloud-connections/verify-a-publisher-connection-from-cloud.md) process to verify that your Publisher is connected to the Portal.
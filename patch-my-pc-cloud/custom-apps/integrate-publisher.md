---
description: Details how to connect the Patch My PC Publisher to our Cloud platform
hidden: true
---

# Integrate Publisher

_Applies to: Custom Apps_

If you plan to use our on-premises Publisher to publish your Custom Apps, you need to integrate it as detailed below before you can create a Custom App.

{% hint style="info" %}
**Note**

If you only plan to use Intune Apps for Cloud to deploy your Custom Apps, you do not need to complete this process and can now [Create a Custom App](create-a-custom-app/).
{% endhint %}

To connect Publisher to PMPC Cloud:

1. Load the **Patch My PC Publishing Service** (Publisher) and verify you are running at least version 2.1.20.0. If you are not, upgrade to the latest version.
2. Click the **Cloud** tab.

{% hint style="success" %}
Tip

If the **Cloud** tab is not present, check you have entered your license key and clicked **Validate**.
{% endhint %}

![&#x22;Cloud&#x22; tab of our Publisher](/_images/image-%281725%29.png-"&#x22;Cloud&#x22;-tab-of-our-Publisher" "&#x22;Cloud&#x22; tab of our Publisher")

3. In the **Connection Name** field, enter a unique name for the connection. For example **Patch My PC Custom Apps**, then click **Connect**.

{% hint style="info" %}
**Note**

The name you enter here determines how this connection shows on the **Connections** page of the **portal**.
{% endhint %}

![Entering a “Connection Name” and clicking “Connect”](/_images/image-%281726%29.png-"Entering-a-\"Connection-Name\"-and-clicking-\"Connect\"" "Entering a “Connection Name” and clicking “Connect”")

4.  In your browser, enter the Entra ID you used to onboard to PMPC Cloud or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.



    ![“Microsoft Sign in” screen](/_images/image-%281420%29.png-"\"Microsoft-Sign-in\"-screen" "“Microsoft Sign in” screen")


5.  Enter the password and click **Sign in**.



    ![“Enter password” screen](/_images/image-%281421%29.png-"\"Enter-password\"-screen" "“Enter password” screen")

    \
    If the connection is successful, a new browser tab opens with the following message:

    **Authentication complete. You can return to the application. Feel free to close this browser tab.**\
    \
    You can close this tab at this point.\

6. If the **Edit a customer** screen is not displayed, proceed to Step 8.
7.  If the **Edit a customer** screen is displayed, click to select the customer you want to connect to, then click **OK**.\


    ![Selecting the relevant customer from the “Edit a customer” screen](/_images/image-%28910%29.png-"Selecting-the-relevant-customer-from-the-\"Edit-a-customer\"-screen" "Selecting the relevant customer from the “Edit a customer” screen")


8.  In Publisher, verify the **Connection Status** shows as **Connected**, then click **Save and Close**.\


    ![Publisher showing it’s “Connected”](/_images/image-%281728%29.png-"Publisher-showing-it’s-\"Connected\"" "Publisher showing it’s “Connected”")

{% hint style="info" %}
**Note**

You can also use the [Verifying the Publisher connection from the Portal](../cloud-administration/manage-cloud-connections/verify-a-publisher-connection-from-cloud.md) process to verify that your Publisher is connected to the Portal.
{% endhint %}


# Add a Connection

_Applies to: Patch My PC Cloud, Publisher_

To connect our on-premises Publisher to Patch My PC (PMPC) Cloud, you need to:

1. Load the **Patch My PC Publishing Service** (Publisher) and verify you are running at least version 2.1.20.0. If you are not, upgrade to the latest version.
2. Click the **Cloud** tab.

{% hint style="success" %}
**Tip**

If the **Cloud** tab is not present, check you have entered your license key and clicked **Validate**.
{% endhint %}

![&#x22;Cloud&#x22; tab of our Publisher](/_images/image-(1725).png "&#x22;Cloud&#x22; tab of our Publisher")

6. In the **Connection Name** field, enter a unique name for the connection. For example **Patch My PC Custom Apps**, then click **Connect**.

{% hint style="info" %}
**Note**

The name you enter here determines how this connection shows on the **Connections** page of the **portal**.
{% endhint %}

![Entering a “Connection Name” and clicking “Connect”](/_images/image-(1726).png "Entering a “Connection Name” and clicking “Connect”")

7.  In your browser, enter the Entra ID you used to onboard to PMPC Cloud or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.\


    ![“Microsoft Sign in” screen](/_images/image-(1420).png "“Microsoft Sign in” screen")


8.  Enter the password and click **Sign in**.\


    ![“Enter password” screen](/_images/image-(1421).png "“Enter password” screen")

    \
    If the connection is successful, a new browser tab opens with the following message:

    **Authentication complete. You can return to the application. Feel free to close this browser tab.**\
    \
    You can close this tab at this point.
9. If the **Edit a customer** screen is not displayed, proceed to Step 11.
10. If the **Edit a customer** screen is displayed, click to select the customer you want to connect to, then click **OK**.\


    ![Selecting the relevant customer from the “Edit a customer” screen](/_images/image-(910).png "Selecting the relevant customer from the “Edit a customer” screen")


11. In Publisher, verify the **Connection Status** shows as **Connected**, then click **Save and Close**.\


    ![Publisher showing it’s “Connected”](/_images/image-(1728).png "Publisher showing it’s “Connected”")

{% hint style="info" %}
**Note**

You can also use the [Verify the Publisher connection](verify-a-publisher-connection-from-cloud.md) process to verify that your Publisher is connected to the portal.
{% endhint %}
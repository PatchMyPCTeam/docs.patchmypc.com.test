---
description: Details how to connect the Patch My PC Publisher to our Cloud platform
hidden: true
---

# Integrate Publisher

_Applies to: Custom Apps_

If you plan to use our on-premises Publisher to publish your Custom Apps, you need to integrate it as detailed below before you can create a Custom App.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If you only plan to use Intune Apps for Cloud to deploy your Custom Apps, you do not need to complete this process and can now [Create a Custom App](create-a-custom-app/).</p>
</blockquote>

To connect Publisher to PMPC Cloud:

1. Load the <strong>Patch My PC Publishing Service</strong> (Publisher) and verify you are running at least version 2.1.20.0. If you are not, upgrade to the latest version.
2. Click the <strong>Cloud</strong> tab.

<blockquote class="wp-block-quote">
<p>Tip</p>
<p>If the <strong>Cloud</strong> tab is not present, check you have entered your license key and clicked <strong>Validate</strong>.</p>
</blockquote>

![&#x22;Cloud&#x22; tab of our Publisher](/_images/image-(1725).png "&#x22;Cloud&#x22; tab of our Publisher")

3. In the <strong>Connection Name</strong> field, enter a unique name for the connection. For example <strong>Patch My PC Custom Apps</strong>, then click <strong>Connect</strong>.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>The name you enter here determines how this connection shows on the <strong>Connections</strong> page of the <strong>portal</strong>.</p>
</blockquote>

![Entering a “Connection Name” and clicking “Connect”](/_images/image-(1726).png "Entering a “Connection Name” and clicking “Connect”")

4.  In your browser, enter the Entra ID you used to onboard to PMPC Cloud or click to select the relevant account from the list of already signed-in accounts. Then click <strong>Next</strong>.



    ![“Microsoft Sign in” screen](/_images/image-(1420).png "“Microsoft Sign in” screen")


5.  Enter the password and click <strong>Sign in</strong>.



    ![“Enter password” screen](/_images/image-(1421).png "“Enter password” screen")

    \
    If the connection is successful, a new browser tab opens with the following message:

    <strong>Authentication complete. You can return to the application. Feel free to close this browser tab.</strong>\
    \
    You can close this tab at this point.\

6. If the <strong>Edit a customer</strong> screen is not displayed, proceed to Step 8.
7.  If the <strong>Edit a customer</strong> screen is displayed, click to select the customer you want to connect to, then click <strong>OK</strong>.\


    ![Selecting the relevant customer from the “Edit a customer” screen](/_images/image-(910).png "Selecting the relevant customer from the “Edit a customer” screen")


8.  In Publisher, verify the <strong>Connection Status</strong> shows as <strong>Connected</strong>, then click <strong>Save and Close</strong>.\


    ![Publisher showing it’s “Connected”](/_images/image-(1728).png "Publisher showing it’s “Connected”")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>You can also use the [Verifying the Publisher connection from the Portal](../cloud-administration/manage-cloud-connections/verify-a-publisher-connection-from-cloud.md) process to verify that your Publisher is connected to the Portal.</p>
</blockquote>
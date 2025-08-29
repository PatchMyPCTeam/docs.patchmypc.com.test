# Add a Company to Manage (Cloud MSP)

_Applies to: Patch My PC Cloud_

Once the parent MSP company has been configured in Patch My PC (PMPC) Cloud with an MSP Plus license, you can add the relevant child companies to be managed.

{% hint style="warning" %}
**Important**

We currently do not support a parent MSP company from taking over the management of an existing child PMPC Cloud company.
{% endhint %}

To add a new PMPC Cloud company to be managed using the MSP Feature:

1. Sign in to the parent company where the MSP license has been enabled.
2.  Click the **MSP Customers** node.

    <figure><img src="../../../../_images/gitbook/image%20%282074%29.png" alt="Clicking the “MSP Customers” node" width="563"><figcaption></figcaption></figure>


3.  On the **MSP Customers** page, click **Add Customer**.

    <figure><img src="../../../../_images/gitbook/image%20%282075%29.png" alt="Clicking “Add Customer”" width="563"><figcaption></figcaption></figure>


4.  Click **Connect** under the **Intune Connection** section.

    <figure><img src="../../../../_images/gitbook/image%20%282301%29.png" alt="Clicking &#x22;Connect&#x22; under the &#x22;Intune Connection&#x22; section of the &#x22;Create New Customer&#x22; screen." width="251"><figcaption></figcaption></figure>


5.  On the **Sign in** screen, enter the Entra ID that is a Global Admin in the child company or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.\


    <figure><img src="../../../../_images/gitbook/image%20%282078%29.png" alt="“Sign in” screen" width="510"><figcaption></figcaption></figure>


6.  Enter the password and click **Sign in**.

    <figure><img src="../../../../_images/gitbook/image%20%282079%29.png" alt="Entering the password and clicking “Sign in”" width="515"><figcaption></figcaption></figure>


7. On the **Permissions requested** screen, click **Accept**.

{% hint style="info" %}
**Note**

The account you are using to connect to the child company’s Intune tenant needs to have the **Global Administrator** role in the child company’s Entra ID to approve the PMPC Cloud enterprise app.

We require these permissions to connect to the child company’s Intune tenant.

See [Permissions required for the Intune Apps](../../../cloud-reference/cloud-permissions-reference/permissions-required-for-intune-apps.md) for more details.
{% endhint %}

<figure><img src="../../../../_images/gitbook/image%20%282080%29.png" alt="Clicking “Accept” on the “Permissions requested” page" width="512"><figcaption></figcaption></figure>

{% hint style="success" %}
**Tip**

You can click the down arrow beside each permission to get more information.
{% endhint %}

8.  Verify Intune has **Connected** successfully.\


    <figure><img src="../../../../_images/gitbook/image%20%282304%29.png" alt="" width="254"><figcaption></figcaption></figure>


9. On the **Create New Customer** page, enter the name of the customer to be managed in the **Customer Name** field.

{% hint style="info" %}
**Note**

We support the characters **À-ÿ** (which includes characters from the Latin-1 Supplement Unicode block) for customer names.
{% endhint %}

<figure><img src="../../../../_images/gitbook/image%20%282308%29.png" alt="Enter the name of the customer in the &#x22;Customer Name&#x22; field" width="252"><figcaption></figcaption></figure>

10. Click **Terms and Conditions**.\


    <figure><img src="../../../../_images/gitbook/image%20%282309%29.png" alt="Clicking &#x22;Terms and Conditions&#x22;." width="252"><figcaption></figcaption></figure>


11. Review the Terms and Conditions, and once you are happy, click the **X** in the top right-hand corner to return to the **Create New Customer** screen.\


    <figure><img src="../../../../_images/gitbook/image%20%282307%29.png" alt="Reviewing the Terms and Conditions" width="563"><figcaption></figcaption></figure>


12. Check the **Accept all Terms and conditions** checkbox, then click **Create**.\


    <figure><img src="../../../../_images/gitbook/image%20%282310%29.png" alt="Accepting the Terms and conditions then clicking &#x22;Create&#x22;." width="257"><figcaption></figcaption></figure>



The portal refreshes, showing the newly added customer and the **Success - Child Customer <**_**customer\_name**_**> created** notification.

<figure><img src="../../../../_images/gitbook/image%20%282566%29.png" alt="Portal refreshing showing the newly added customer and the &#x22;Success - Child Customer <customer_name> created&#x22; notification." width="563"><figcaption></figcaption></figure>

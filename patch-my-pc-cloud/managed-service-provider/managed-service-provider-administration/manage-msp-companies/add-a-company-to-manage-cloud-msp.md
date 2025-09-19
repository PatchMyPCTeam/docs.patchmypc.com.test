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

    !\[]\(/\_images/image-(2074 "").png "")
3.  On the **MSP Customers** page, click **Add Customer**.

    !\[]\(/\_images/image-(2075 "").png "")
4.  Click **Connect** under the **Intune Connection** section.

    !\[]\(/\_images/image-(2301 "").png "")
5.  On the **Sign in** screen, enter the Entra ID that is a Global Admin in the child company or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.\\

    !\[]\(/\_images/image-(2078 "").png "")
6.  Enter the password and click **Sign in**.

    !\[]\(/\_images/image-(2079 "").png "")
7. On the **Permissions requested** screen, click **Accept**.

{% hint style="info" %}
**Note**

The account you are using to connect to the child company’s Intune tenant needs to have the **Global Administrator** role in the child company’s Entra ID to approve the PMPC Cloud enterprise app.

We require these permissions to connect to the child company’s Intune tenant.

See [Permissions required for the Intune Apps](../../../cloud-reference/cloud-permissions-reference/permissions-required-for-intune-apps.md) for more details.
{% endhint %}

!\[]\(/\_images/image-(2080 "").png "")

{% hint style="success" %}
**Tip**

You can click the down arrow beside each permission to get more information.
{% endhint %}

8.  Verify Intune has **Connected** successfully.\\

    !\[]\(/\_images/image-(2304 "").png "")
9. On the **Create New Customer** page, enter the name of the customer to be managed in the **Customer Name** field.

{% hint style="info" %}
**Note**

We support the characters **À-ÿ** (which includes characters from the Latin-1 Supplement Unicode block) for customer names.
{% endhint %}

!\[]\(/\_images/image-(2308 "").png "")

10. Click **Terms and Conditions**.\\

    !\[]\(/\_images/image-(2309 "").png "")
11. Review the Terms and Conditions, and once you are happy, click the **X** in the top right-hand corner to return to the **Create New Customer** screen.\\

    !\[]\(/\_images/image-(2307 "").png "")
12. Check the **Accept all Terms and conditions** checkbox, then click **Create**.\\

    !\[]\(/\_images/image-(2310 "").png "")

The portal refreshes, showing the newly added customer and the **Success - Child Customer <**_**customer\_name**_**> created** notification.

!\[]\(/\_images/image-(2566 "").png "") created" notification." width="563">

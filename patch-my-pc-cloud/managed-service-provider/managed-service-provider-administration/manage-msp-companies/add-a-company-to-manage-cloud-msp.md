# Add a Company to Manage (Cloud MSP)

_Applies to: Patch My PC Cloud_

Once the parent MSP company has been configured in Patch My PC (PMPC) Cloud with an MSP Plus license, you can add the relevant child companies to be managed.

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>We currently do not support a parent MSP company from taking over the management of an existing child PMPC Cloud company.</p>
</blockquote>

To add a new PMPC Cloud company to be managed using the MSP Feature:

1. Sign in to the parent company where the MSP license has been enabled.
2.  Click the **MSP Customers** node.

    ![Clicking the “MSP Customers” node](/_images/image-(2074 "Clicking the “MSP Customers” node").png "Clicking the “MSP Customers” node")


3.  On the **MSP Customers** page, click **Add Customer**.

    ![Clicking “Add Customer”](/_images/image-(2075 "Clicking “Add Customer”").png "Clicking “Add Customer”")


4.  Click **Connect** under the **Intune Connection** section.

    ![Clicking &#x22;Connect&#x22; under the &#x22;Intune Connection&#x22; section of the &#x22;Create New Customer&#x22; screen.](/_images/image-(2301 "Clicking &#x22;Connect&#x22; under the &#x22;Intune Connection&#x22; section of the &#x22;Create New Customer&#x22; screen.").png "Clicking &#x22;Connect&#x22; under the &#x22;Intune Connection&#x22; section of the &#x22;Create New Customer&#x22; screen.")


5.  On the **Sign in** screen, enter the Entra ID that is a Global Admin in the child company or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.\


    ![“Sign in” screen](/_images/image-(2078 "“Sign in” screen").png "“Sign in” screen")


6.  Enter the password and click **Sign in**.

    ![Entering the password and clicking “Sign in”](/_images/image-(2079 "Entering the password and clicking “Sign in”").png "Entering the password and clicking “Sign in”")


7. On the **Permissions requested** screen, click **Accept**.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>The account you are using to connect to the child company’s Intune tenant needs to have the **Global Administrator** role in the child company’s Entra ID to approve the PMPC Cloud enterprise app.</p>
<p>We require these permissions to connect to the child company’s Intune tenant.</p>
<p>See [Permissions required for the Intune Apps](../../../cloud-reference/cloud-permissions-reference/permissions-required-for-intune-apps.md) for more details.</p>
</blockquote>

![Clicking “Accept” on the “Permissions requested” page](/_images/image-(2080 "Clicking “Accept” on the “Permissions requested” page").png "Clicking “Accept” on the “Permissions requested” page")

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>You can click the down arrow beside each permission to get more information.</p>
</blockquote>

8.  Verify Intune has **Connected** successfully.\


    ![](/_images/image-(2304).png "")


9. On the **Create New Customer** page, enter the name of the customer to be managed in the **Customer Name** field.

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>We support the characters **À-ÿ** (which includes characters from the Latin-1 Supplement Unicode block) for customer names.</p>
</blockquote>

![Enter the name of the customer in the &#x22;Customer Name&#x22; field](/_images/image-(2308 "Enter the name of the customer in the &#x22;Customer Name&#x22; field").png "Enter the name of the customer in the &#x22;Customer Name&#x22; field")

10. Click **Terms and Conditions**.\


    ![Clicking &#x22;Terms and Conditions&#x22;.](/_images/image-(2309 "Clicking &#x22;Terms and Conditions&#x22;.").png "Clicking &#x22;Terms and Conditions&#x22;.")


11. Review the Terms and Conditions, and once you are happy, click the **X** in the top right-hand corner to return to the **Create New Customer** screen.\


    ![Reviewing the Terms and Conditions](/_images/image-(2307 "Reviewing the Terms and Conditions").png "Reviewing the Terms and Conditions")


12. Check the **Accept all Terms and conditions** checkbox, then click **Create**.\


    ![Accepting the Terms and conditions then clicking &#x22;Create&#x22;.](/_images/image-(2310 "Accepting the Terms and conditions then clicking &#x22;Create&#x22;.").png "Accepting the Terms and conditions then clicking &#x22;Create&#x22;.")



The portal refreshes, showing the newly added customer and the **Success - Child Customer <**_**customer\_name**_**> created** notification.

![](/_images/image-(2566).png "")
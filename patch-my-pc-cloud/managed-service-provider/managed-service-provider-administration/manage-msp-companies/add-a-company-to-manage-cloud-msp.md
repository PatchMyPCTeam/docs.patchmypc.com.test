# Add a Company to Manage (Cloud MSP)

_Applies to: Patch My PC Cloud_

Once the parent MSP company has been configured in Patch My PC (PMPC) Cloud with an MSP Plus license, you can add the relevant child companies to be managed.

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>We currently do not support a parent MSP company from taking over the management of an existing child PMPC Cloud company.</p>
</blockquote>

To add a new PMPC Cloud company to be managed using the MSP Feature:

1. Sign in to the parent company where the MSP license has been enabled.
2.  Click the <strong>MSP Customers</strong> node.

    ![Clicking the “MSP Customers” node](/_images/image-(2074).png "Clicking the “MSP Customers” node")


3.  On the <strong>MSP Customers</strong> page, click <strong>Add Customer</strong>.

    ![Clicking “Add Customer”](/_images/image-(2075).png "Clicking “Add Customer”")


4.  Click <strong>Connect</strong> under the <strong>Intune Connection</strong> section.

    ![Clicking &#x22;Connect&#x22; under the &#x22;Intune Connection&#x22; section of the &#x22;Create New Customer&#x22; screen.](/_images/image-(2301).png "Clicking &#x22;Connect&#x22; under the &#x22;Intune Connection&#x22; section of the &#x22;Create New Customer&#x22; screen.")


5.  On the <strong>Sign in</strong> screen, enter the Entra ID that is a Global Admin in the child company or click to select the relevant account from the list of already signed-in accounts. Then click <strong>Next</strong>.\


    ![“Sign in” screen](/_images/image-(2078).png "“Sign in” screen")


6.  Enter the password and click <strong>Sign in</strong>.

    ![Entering the password and clicking “Sign in”](/_images/image-(2079).png "Entering the password and clicking “Sign in”")


7. On the <strong>Permissions requested</strong> screen, click <strong>Accept</strong>.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>The account you are using to connect to the child company’s Intune tenant needs to have the <strong>Global Administrator</strong> role in the child company’s Entra ID to approve the PMPC Cloud enterprise app.</p>
<p>We require these permissions to connect to the child company’s Intune tenant.</p>
<p>See [Permissions required for the Intune Apps](../../../cloud-reference/cloud-permissions-reference/permissions-required-for-intune-apps.md) for more details.</p>
</blockquote>

![Clicking “Accept” on the “Permissions requested” page](/_images/image-(2080).png "Clicking “Accept” on the “Permissions requested” page")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>You can click the down arrow beside each permission to get more information.</p>
</blockquote>

8.  Verify Intune has <strong>Connected</strong> successfully.\


    ![](/_images/image-(2304).png "")


9. On the <strong>Create New Customer</strong> page, enter the name of the customer to be managed in the <strong>Customer Name</strong> field.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>We support the characters <strong>À-ÿ</strong> (which includes characters from the Latin-1 Supplement Unicode block) for customer names.</p>
</blockquote>

![Enter the name of the customer in the &#x22;Customer Name&#x22; field](/_images/image-(2308).png "Enter the name of the customer in the &#x22;Customer Name&#x22; field")

10. Click <strong>Terms and Conditions</strong>.\


    ![Clicking &#x22;Terms and Conditions&#x22;.](/_images/image-(2309).png "Clicking &#x22;Terms and Conditions&#x22;.")


11. Review the Terms and Conditions, and once you are happy, click the <strong>X</strong> in the top right-hand corner to return to the <strong>Create New Customer</strong> screen.\


    ![Reviewing the Terms and Conditions](/_images/image-(2307).png "Reviewing the Terms and Conditions")


12. Check the <strong>Accept all Terms and conditions</strong> checkbox, then click <strong>Create</strong>.\


    ![Accepting the Terms and conditions then clicking &#x22;Create&#x22;.](/_images/image-(2310).png "Accepting the Terms and conditions then clicking &#x22;Create&#x22;.")



The portal refreshes, showing the newly added customer and the <strong>Success - Child Customer <</strong>_<strong>customer\_name</strong>_<strong>> created</strong> notification.

![](/_images/image-(2566).png "")
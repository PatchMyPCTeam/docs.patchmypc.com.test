# Add a Company to Manage (Cloud MSP)

_Applies to: Patch My PC Cloud_

Once the parent MSP company has been configured in Patch My PC (PMPC) Cloud with an MSP Plus license, you can add the relevant child companies to be managed.

> **Important**
>
> We currently do not support a parent MSP company from taking over the management of an existing child PMPC Cloud company.

To add a new PMPC Cloud company to be managed using the MSP Feature:

1. Sign in to the parent company where the MSP license has been enabled.
2.  Click the **MSP Customers** node.

    ![Clicking the “MSP Customers” node](../../../../.gitbook/assets/image-\(2074\).png)
3.  On the **MSP Customers** page, click **Add Customer**.

    ![Clicking “Add Customer”](../../../../.gitbook/assets/image-\(2075\).png)
4.  Click **Connect** under the **Intune Connection** section.

    ![Clicking "Connect" under the "Intune Connection" section of the "Create New Customer" screen.](../../../../.gitbook/assets/image-\(2301\).png)
5.  On the **Sign in** screen, enter the Entra ID that is a Global Admin in the child company or click to select the relevant account from the list of already signed-in accounts. Then click **Next**.\\

    ![“Sign in” screen](../../../../.gitbook/assets/image-\(2078\).png)
6.  Enter the password and click **Sign in**.

    ![Entering the password and clicking “Sign in”](../../../../.gitbook/assets/image-\(2079\).png)
7. On the **Permissions requested** screen, click **Accept**.

> **Note**
>
> The account you are using to connect to the child company’s Intune tenant needs to have the **Global Administrator** role in the child company’s Entra ID to approve the PMPC Cloud enterprise app.
>
> We require these permissions to connect to the child company’s Intune tenant.
>
> See \[Permissions required for the Intune Apps]\(../../../cloud-reference/cloud-permissions-reference/permissions-required-for-intune-apps.md) for more details.

![Clicking “Accept” on the “Permissions requested” page](../../../../.gitbook/assets/image-\(2080\).png)

> **Tip**
>
> You can click the down arrow beside each permission to get more information.

8.  Verify Intune has **Connected** successfully.\\

    ![](../../../../.gitbook/assets/image-\(2304\).png)
9. On the **Create New Customer** page, enter the name of the customer to be managed in the **Customer Name** field.

> **Note**
>
> We support the characters **À-ÿ** (which includes characters from the Latin-1 Supplement Unicode block) for customer names.

![Enter the name of the customer in the "Customer Name" field](../../../../.gitbook/assets/image-\(2308\).png)

10. Click **Terms and Conditions**.\\

    ![Clicking "Terms and Conditions".](../../../../.gitbook/assets/image-\(2309\).png)
11. Review the Terms and Conditions, and once you are happy, click the **X** in the top right-hand corner to return to the **Create New Customer** screen.\\

    ![Reviewing the Terms and Conditions](../../../../.gitbook/assets/image-\(2307\).png)
12. Check the **Accept all Terms and conditions** checkbox, then click **Create**.\\

    ![Accepting the Terms and conditions then clicking "Create".](../../../../.gitbook/assets/image-\(2310\).png)

The portal refreshes, showing the newly added customer and the **Success - Child Customer <**_**customer\_name**_**> created** notification.

![](../../../../.gitbook/assets/image-\(2566\).png)

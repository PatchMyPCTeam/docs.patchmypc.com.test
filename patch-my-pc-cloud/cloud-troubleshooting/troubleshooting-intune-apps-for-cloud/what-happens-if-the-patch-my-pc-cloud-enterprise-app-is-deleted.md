# What happens if the Patch My PC Cloud Enterprise App is deleted?

_Applies to: Intune Apps for Cloud_

If you have onboarded successfully to Patch My PC (PMPC) Cloud and someone deletes the **Patch My PC Cloud** Enterprise Application, you will experience the following behavior:

*   **Intune Apps –** Any apps already deployed using Intune Apps for Cloud will remain there. When you try to deploy any new apps, you will receive a **500 Internal Server Error** when trying to add an assignment.\


    ![500 Internal Server Error](/_images/image-(794).png "500 Internal Server Error")

    \
    Even if you ignore this and continue, your deployments will stay stuck with a **Status** of **In Progress**.
*   **Custom Apps –** If you sign out of the portal after our Enterprise App has been deleted, the next time you sign back in again, you will see the **Permissions requested** dialog box. Clicking **Accept** will recreate the **Patch My PC Cloud** Enterprise Application registration.\


    ![Permissions requested dialog box](/_images/image-(796).png "Permissions requested dialog box")


# Edit Update Rings in Cloud

_Applies to: Patch My PC Cloud_

{% hint style="warning" %}
**Important**

If a Patch My PC (PMPC) Cloud deployment is created with [Delayed Update Rings](how-cloud-update-rings-are-created.md#delayed-update-rings), you cannot edit it until all of the rings have been created. If you attempt to edit a deployment with incomplete  Update Rings you will see the [Error - Editing is not allowed until all rings are created after the configured delay](../../cloud-troubleshooting/troubleshooting-cloud-update-rings/error-editing-is-not-allowed-until-all-rings-are-created-after-the-configured-delay-cloud-error.md) message.

Also, if you make any changes to Return Codes for a deployment where Update Rings are enabled, these changes are only applied to the latest ring (newest version).
{% endhint %}

To edit the Update Rings configuration for a deployment:

1.  Navigate to the **Deployments** node.\


    ![Navigating to the “Deployments” node](../../../_images/image%20%28434%29.png%20"Navigating%20to%20the%20\"Deployments\"%20node")


2. Click the relevant deployment whose Update Ring configuration you want to edit.

{% hint style="success" %}
**Tip**

Click the filter button (![](../../../_images/image%20%282513).png>)) and select the **Enabled** option under the **Update Rings** section, followed by **Apply Filters** to see just those deployments that have update Rings configured.&#x20;
{% endhint %}

![Clicking the relevant deployment you want to edit](../../../_images/image%20%282060%29.png%20"Clicking%20the%20relevant%20deployment%20you%20want%20to%20edit")

3.  Click **Edit**.\


    ![Clicking “More Info”](../../../_images/image%20%28436%29.png%20"Clicking%20\"More%20Info\"")


4.  Click the **Assignments** tab.\


    ![Clicking the “Assignments” tab](../../../_images/image%20%28437%29.png%20"Clicking%20the%20\"Assignments\"%20tab")


5. Make any required changes, for example:&#x20;
   1. Move Assignments between rings using drag and drop
   2. Rename rings by clicking the pencil icon beside the relevant ring
   3. Modify the delay for a ring by clicking the minus (**-**) or plus (**+**)
   4. Add a ring by clicking **Add Update Rings**
   5. Delete a ring by clicking the red x after the delay.
6.  Click **Save** to save your changes.\


    ![Clicking “Save”](../../../_images/image%20%28438%29.png%20"Clicking%20\"Save\"")

    \
    If you make any changes that affect how the Update Rings will work, you will see the **“<**_**app\_name**_**>” Deployment Summary** asking you to either confirm or cancel your changes.\
    \
    For example, reducing the delay for **Corel All Users** ring from **3** days to **2** results in the following.\


    ![Example “Deployment Summary” showing the effects of the edit](../../../_images/image%20%28439%29.png%20"Example%20\"Deployment%20Summary\"%20showing%20the%20effects%20of%20the%20edit")


7.  Either click **Cancel** to return to the **Assignments** tab and make any required changes or click **Confirm** to save your changes.\
    \
    The **Deployments** node is redisplayed along with the **Success – Edited <**_**deployment\_name**_**>** notification.\


    ![](../../../_images/image%20%28440%29.png%20"")

# Return Codes (Deployments)

_Applies to: Patch My PC Cloud_

{% hint style="info" %}
**Note**

Using the **Return Codes** tool is optional.
{% endhint %}

The **Return Codes** tool of the Patch My PC (PMPC) Cloud deployment wizard allows you to configure _Return Codes_ for a deployment (a _Return Code_ is a numerical code an app typically logs and reports once it has completed running its installer).

You can manage Return Codes from within the properties of a:

* Deployment
* Custom App

{% hint style="info" %}
**Note**

See the [Configuration ](../../../custom-apps/create-a-custom-app/custom-apps-configuration-tab.md)section of [Create a Custom App](../../../custom-apps/create-a-custom-app/) for details on how to configure Return Codes within the properties of a Custom App.

Also, macOS apps also do not support Return Codes.
{% endhint %}

To manage Return Codes for a Deployment:

1. Click the **Return Codes** tool.

![Clicking the “Return Codes” tool](../../../../_images/image%20%2862%29.png%20"Clicking%20the%20\"Return%20Codes\"%20tool")

2. Scroll down to the **Manage Return Codes** section, which shows the default Return Codes plus any defined for the app if this is a Custom App.

{% hint style="info" %}
**Note**

If a vendor supplies a list of Return Codes for their app, we include it. If they don’t, we automatically populate the list of Return Codes with industry-standard codes.
{% endhint %}

![Scrolling down to the “Manage Return Codes” section](../../../../_images/image%20%2863%29.png%20"Scrolling%20down%20to%20the%20\"Manage%20Return%20Codes\"%20section")

3. If you do not want to add a new Return Code, proceed to Step 5.
4. To add a new Return Code for this deployment, enter the numerical value in the **Return Code** field, select its meaning from the **Code type** dropdown, then click **Add**.

![Adding a new Return Code](../../../../_images/image%20%2864%29.png%20"Adding%20a%20new%20Return%20Code")

The new Return Code is added to the list.

![New Return Code added to the list.](../../../../_images/image%20%2865%29.png%20"New%20Return%20Code%20added%20to%20the%20list.")

5. If you do not want to edit a Return Code, go to Step 9.
6. To edit a Return Code, click the pencil icon beside it.

![Clicking the pencil icon beside a Return Code to edit it.](../../../../_images/image%20%2866%29.png%20"Clicking%20the%20pencil%20icon%20beside%20a%20Return%20Code%20to%20edit%20it.")

7. Make any required changes.
8. Click the green tick to save your changes.

![Clicking the green tick to save your changes](../../../../_images/image%20%2867%29.png%20"Clicking%20the%20green%20tick%20to%20save%20your%20changes")

The **Code type** field is updated.

![“Code type” field updated.](../../../../_images/image%20%2868%29.png%20"\"Code%20type\"%20field%20updated.")

9. If you do not want to delete a Return Code, go to Step 11.
10. To delete a Return Code, click the red trash can beside the relevant code.

{% hint style="info" %}
**Note**

You cannot delete either the default Return Codes for a deployment or any that have been added as part of the Custom App’s configuration. However, you can edit them.

If you add a Return Code to a deployment, you will be able to edit or delete it from the deployment if required.
{% endhint %}

{% hint style="danger" %}
**Important**

If the Return Codes you define in a deployment differ/conflict with those defined for a Custom App, the Return Codes defined on the deployment take precedence.
{% endhint %}

![Deleting a Return Code](../../../../_images/image%20%2869%29.png%20"Deleting%20a%20Return%20Code")

The code is deleted from the list.

![Code deleted from the list](../../../../_images/image%20%2870%29.png%20"Code%20deleted%20from%20the%20list")

11. If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.\
    \
    Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant process.

![Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; tab](../../../../_images/image%20%2871%29.png%20"Clicking%20&#x22;Next&#x22;%20to%20move%20to%20the%20&#x22;Assignments&#x22;%20tab")

{% hint style="info" %}
**Note**

You can use the [Check Return Codes](../../../cloud-reference/intune-reference/check-return-codes-in-intune.md) process to verify your Return Codes have been successfully created in Intune by PMPC Cloud.
{% endhint %}

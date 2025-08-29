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

<figure><img src="../../../../_images/gitbook/image (62).png" alt="Clicking the “Return Codes” tool" width="563"><figcaption></figcaption></figure>

2. Scroll down to the **Manage Return Codes** section, which shows the default Return Codes plus any defined for the app if this is a Custom App.

{% hint style="info" %}
**Note**

If a vendor supplies a list of Return Codes for their app, we include it. If they don’t, we automatically populate the list of Return Codes with industry-standard codes.
{% endhint %}

<figure><img src="../../../../_images/gitbook/image (63).png" alt="Scrolling down to the “Manage Return Codes” section" width="435"><figcaption></figcaption></figure>

3. If you do not want to add a new Return Code, proceed to Step 5.
4. To add a new Return Code for this deployment, enter the numerical value in the **Return Code** field, select its meaning from the **Code type** dropdown, then click **Add**.

<figure><img src="../../../../_images/gitbook/image (64).png" alt="Adding a new Return Code" width="436"><figcaption></figcaption></figure>

The new Return Code is added to the list.

<figure><img src="../../../../_images/gitbook/image (65).png" alt="New Return Code added to the list." width="419"><figcaption></figcaption></figure>

5. If you do not want to edit a Return Code, go to Step 9.
6. To edit a Return Code, click the pencil icon beside it.

<figure><img src="../../../../_images/gitbook/image (66).png" alt="Clicking the pencil icon beside a Return Code to edit it." width="419"><figcaption></figcaption></figure>

7. Make any required changes.
8. Click the green tick to save your changes.

<figure><img src="../../../../_images/gitbook/image (67).png" alt="Clicking the green tick to save your changes" width="422"><figcaption></figcaption></figure>

The **Code type** field is updated.

<figure><img src="../../../../_images/gitbook/image (68).png" alt="“Code type” field updated." width="420"><figcaption></figcaption></figure>

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

<figure><img src="../../../../_images/gitbook/image (69).png" alt="Deleting a Return Code" width="420"><figcaption></figcaption></figure>

The code is deleted from the list.

<figure><img src="../../../../_images/gitbook/image (70).png" alt="Code deleted from the list" width="425"><figcaption></figcaption></figure>

11. If you do not want to configure any of the optional tabs under the **Tools** section, click **Next** to move to the [Assignments](../cloud-assignments-deployment-tab.md) tab.\
    \
    Otherwise, click on the relevant tab under **Tools** to configure the required settings, which are explained in the relevant process.

<figure><img src="../../../../_images/gitbook/image (71).png" alt="Clicking &#x22;Next&#x22; to move to the &#x22;Assignments&#x22; tab" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**

You can use the [Check Return Codes](../../../cloud-reference/intune-reference/check-return-codes-in-intune.md) process to verify your Return Codes have been successfully created in Intune by PMPC Cloud.
{% endhint %}

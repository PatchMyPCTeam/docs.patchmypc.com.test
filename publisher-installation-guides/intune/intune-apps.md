---
description: >-
  Enabling and creating Intune Applications in the Patch My PC publishing
  service.
---

# Intune Apps

_Applies to: On-premises Publisher_

## Feature Enablement&#x20;

To enable products to publish, check the "<strong>Enable creation of Win32 applications in Microsoft Intune</strong>" checkbox.

![Intune App Enablement](/_images/FeatureEnablement_IntuneApps.png)

Once the option is selected, you'll be able to enable other products. When first getting started with the product, it is recommended that you only <strong>choose one or two products</strong> to reduce the impact on the first sync and to validate your implementation quickly. We have found that <strong>Notepad++</strong> and <strong>7-Zip</strong> tend to be great initial use case tests.

<blockquote class="wp-block-quote">
<p><strong>Tip</strong>: We recommend enabling <strong>Manage Conflicting Processes</strong> for <strong>Notepad++</strong></p>
</blockquote>

{% embed url="https://patchmypc.com/manage-conflicting-processes-when-updating-third-party-applications" %}

To find and enable these products, you can search the list of products using <strong>Ctrl + F</strong> or by clicking on the magnifying glass in the lower right corner.&#x20;

![Select the search option](/_images/Search_IntuneApps.png)

When you select the search button a dialogue will open, type in one of our example products and hit enter, or click OK.

![Search for product](/_images/SearchTerms.png)

Once you have found the product you want to patch, click the checkbox for your architecture choice and click <strong>Apply</strong>.

<blockquote class="wp-block-quote">
<p><strong>Tip</strong>: You can right-click All Products, Vendors, or individual Products to apply custom installation options as described in the article below.</p>
</blockquote>

{% embed url="https://patchmypc.com/custom-options-available-for-third-party-updates-and-applications" %}
Custom right-click options for customizing installation behavior
{% endembed %}

![Select and Enable a product](/_images/SelectAppAndApply_IntuneApps.png)

<blockquote class="wp-block-quote">
<p>If you hit <strong>OK</strong>  instead of <strong>Apply</strong>, don't worry as the Publisher will close after saving the changes. You can just re-open and keep right on working.</p>
</blockquote>
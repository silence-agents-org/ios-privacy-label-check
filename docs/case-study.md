# Case study (based on public reporting): when app data sharing contradicted the privacy promise

> **Based entirely on public reporting.** Not a Patterns Lab client; we have not audited these companies. Every figure comes from the cited public source. Web version: https://patternslab.work/case-study

## The pattern
A consumer health app tells users their health data stays private. Its app and website also ship third-party advertising and analytics SDKs that receive identifiers and health-related events. Later, a regulator documents the gap between the promise and the actual data flow.

## GoodRx — FTC, 2023-02-01
- Civil penalty **USD 1.5 million**; first enforcement under the FTC Health Breach Notification Rule.
- Data shared with Facebook, Google, Criteo, Branch and Twilio (per FTC complaint).
- **55 million+** consumers visited or used GoodRx's website or apps since January 2017.
- Order: ban on sharing health data for advertising, affirmative consent for other sharing, deletion requests to third parties, mandated privacy program.

Source: https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising

## BetterHelp — FTC, 2023-03-02
- **USD 7.8 million** for partial refunds to consumers who paid between 2017-08-01 and 2020-12-31.
- Email addresses, IP addresses and health questionnaire information shared with Facebook, Snapchat, Criteo and Pinterest for advertising (per FTC complaint).
- Each future order violation: civil penalty up to **USD 50,120**.

Source: https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-ban-betterhelp-revealing-consumers-data-including-sensitive-mental-health-information-facebook

## The App Store side
Since spring 2024 Apple requires privacy manifests for commonly used third-party SDKs added in new submissions or updates, and approved reasons for "required reason" APIs to upload to App Store Connect. The developer is responsible for all code an SDK includes.

Source: https://developer.apple.com/news/?id=r1henawx (2023-12-07)

## What an endpoint-level check surfaces
Both cases hinge on one testable question: which third parties does the shipped app actually send data to, and does that match what users were told? `check.py` in this repo compares a HAR capture with your App Store privacy label. We make no claim about what outcome a review would have changed in these cases.

- Estimate your exposure: https://patternslab.work/calculator
- Free 15-minute check or full audit (USD 9,000 fixed, 50% upfront): audit@patternslab.work

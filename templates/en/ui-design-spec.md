# UI design specification

> Product / flow:  
> Figma source and version:  
> Design owner:  
> Engineering owner:  
> Status: Draft / Approved / Implemented  
> Target platforms:

## 1. Experience intent

- User goal and emotional/brand intent:
- Primary theme or visual idea:
- What must feel distinctive rather than merely conventional:
- What the AI may implement mechanically:
- What requires explicit human visual approval:

## 2. Source-of-truth rule

Define which Figma page, component library, tokens, assets, copy deck, and interaction notes are authoritative. Screenshots are reference evidence, not a substitute for component semantics and state behavior.

## 3. Screen and state inventory

| Screen / component | Entry | Normal | Loading | Empty | Error | Offline | Permission / disabled | Success |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Unspecified states must not be invented silently. Record the gap and obtain a decision.

## 4. Layout and fidelity constraints

- Breakpoints and device classes:
- Safe areas and system UI:
- Grid, spacing, radius, and elevation tokens:
- Typography and dynamic text scaling:
- Asset source and rendering mode:
- Pixel-diff or screenshot tolerance:
- Intentional platform-native deviations:

## 5. Interaction specification

For each interaction document trigger, feedback, state transition, animation, latency behavior, cancellation, retry, and accessibility behavior.

## 6. Data and copy

- Field semantics and formatting:
- Validation timing and messages:
- Truncation, wrapping, localization expansion:
- Empty and partial data:
- Privacy-sensitive display and masking:

## 7. Accessibility

- Focus order and keyboard behavior:
- Screen-reader labels, roles, hints, and announcements:
- Contrast and non-color cues:
- Motion reduction:
- Touch target and gesture alternatives:
- Caption/transcript needs for audio or video:

## 8. Test plan

- Component/state tests:
- Screenshot or visual regression:
- Critical-flow automation (for example Playwright or Maestro):
- Real-device/browser matrix:
- Accessibility checks:
- Human design review checkpoints:

## 9. Implementation report

| Item | Figma | Implemented | Difference | Reason | Approved by |
|---|---|---|---|---|---|
| | link/frame | link/build | | | |

## 10. Definition of faithful implementation

“100% reproduction” must be operationalized. Define acceptable visual tolerance, required states, interactions, content behavior, accessibility, and the human design sign-off required before the claim can be made.

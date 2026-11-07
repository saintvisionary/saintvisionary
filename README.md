<!-- Profile README: lives in the public repo saintvisionary/saintvisionary -->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=24&duration=3200&pause=900&color=FF9900&center=true&vCenter=true&width=640&lines=Hi%2C+I'm+Tyler+%F0%9F%91%8B;Identity+is+the+new+perimeter.;Securing+humans%2C+machines%2C+and+AI+agents." alt="Hi, I'm Tyler. Identity is the new perimeter. Securing humans, machines, and AI agents." />

**Identity & Access Management · AI Agent Security · Security Operations**

*I secure AI agents, and I use AI agents to secure identity.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-connect-0A66C2?style=flat-square)](https://www.linkedin.com/in/tyler-bynum-838b8132b)
[![Featured](https://img.shields.io/badge/featured-AI_Agent_Spend_Gate-FF9900?style=flat-square)](https://github.com/saintvisionary/AI-Agent-Spend-Gate)
[![Featured](https://img.shields.io/badge/featured-CareMap-30D158?style=flat-square)](https://github.com/saintvisionary/CareMap)

</div>

---

### 🛡️ About me

- I'm a security practitioner focused on **identity**: who and what gets access, to what, for how long, and how you prove it to an auditor.
- My focus is **non-human identity**: giving AI agents and service accounts their own identity, a human owner, least privilege, approval for risky actions, and a full audit trail.
- I build controls, then attack them. Every bypass I find goes into a journal along with how I fixed it.
- I'm starting an **MS in Cybersecurity at Georgia Tech** in January 2027.

### 🔑 Security principles, applied

| Principle | Where it shows up in my work |
|:---|:---|
| **Least privilege** | The agent's AWS IAM policy can invoke one model and nothing else |
| **Separation of duties** | The AI agent proposes a purchase; a separate policy engine decides |
| **Zero trust for inputs** | LLM output and tool results are treated as untrusted, even from internal feeds |
| **Defense in depth** | Three independent layers: the agent, a Decider 2B guardrail, deterministic rules |
| **Fail closed** | Deny by default: unknown vendors, unknown categories and malformed amounts are blocked |
| **Threat modeling** | Prompt injection and excessive agency ([OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/)), business email compromise |
| **Detection & response** | Every guardrail verdict is recorded with a reason and confidence scores, so it can be sent to a SIEM |
| **Adversarial testing** | Found and fixed bypasses: `NaN`, `true`, and fraction-of-a-cent amounts |
| **Data minimization** | CareMap works out eligibility in the browser; the AI agent sees a tier percentage, never a salary |
| **Output integrity** | Every dollar figure an AI reply states must match a tool result, or the reply is forced to rewrite |

---

### 🚀 Featured projects

<div align="center">

<a href="https://github.com/saintvisionary/AI-Agent-Spend-Gate">
  <img src="assets/card-ai-agent-spend-gate.svg" alt="AI Agent Spend Gate" />
</a>

</div>

**[AI Agent Spend Gate](https://github.com/saintvisionary/AI-Agent-Spend-Gate):** *your AI agent has a company card. Here's what keeps it honest.*

```mermaid
flowchart LR
    A["🤖 Agent<br/>Amazon Bedrock<br/><i>proposes</i>"] --> B["🧠 Decider 2B<br/>guardrail<br/><i>is it honest?</i>"]
    B --> C["🛂 Spend Gate<br/>Python rules<br/><i>is it allowed?</i>"]
    C --> D["💳 Order"]
    B -. "unsure" .-> H["🙋 Human"]
    C -. "over limit" .-> H
```

- **Three layers of control.** The LLM proposes, Strands Decider 2B checks honesty (grounded, injected, mislabeled), and a deny-by-default rules engine decides permission.
- **Models can add friction, never approve.** Only the deterministic rules, or a human, can say yes to spending money.
- **Built for prompt injection.** A poisoned note in a tool result tells the agent to buy $450 of gift cards and file them as office supplies. The rules alone would approve that lie. The guardrail catches it and denies it before the tool runs.
- **Calibrated confidence.** Uncertain calls go to a human, not to a guess.
- **Reusable `#guardrails` pattern** that works with any Strands agent.
- **I break my own controls.** The [build journal](https://github.com/saintvisionary/AI-Agent-Spend-Gate/blob/main/JOURNAL.md) records every bypass I found, like a `nan` amount that slipped past every rule, and how I fixed it.

#### 🗺️ CareMap

<div align="center">

<a href="https://github.com/saintvisionary/CareMap">
  <img src="assets/card-caremap.svg" alt="CareMap" />
</a>

</div>

**[CareMap](https://github.com/saintvisionary/CareMap):** *what care would cost you, before the bill.* A map of 4,500+ US hospitals and 11,200 sliding-fee clinics, priced for you under the charity-care law that applies where you live, with the math shown. 17 state laws modeled, each encoded from the statute with its citation.

```mermaid
flowchart LR
    U["👤 You<br/>ZIP, household, income"] --> B["🔒 Browser<br/>poverty-line math,<br/>state rule"]
    B -- "tier % only" --> A["🤖 Strands agent<br/>AWS Lambda"]
    A --> T["🧾 Tools<br/>CMS + state law"]
    T --> G["🛂 Grounding guard<br/><i>every $ from a tool?</i>"]
    G -. "no: rewrite" .-> A
    G --> R["💬 Reply + map"]
```

- **Privacy by design.** Household size and income are redacted in the browser before any network call; the agent only ever sees a tier and a ZIP.
- **AI output is untrusted.** Strands hooks keep a ledger of every number a tool returned; a reply that states a figure not in the ledger is sent back to be rewritten.
- **Works without the AI.** The map, prices and law math run client-side, so the app keeps working when the model is down or out of quota.
- **Hardened endpoint.** The Lambda Function URL has a CORS allow-list, a max message length and a per-IP rate limit.
- **Tested and accessible.** 240 tests (Python and TypeScript) and an automated WCAG 2.2 AA audit.

---

### 🧰 Toolbox

**Working with**

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS" />
<img src="https://img.shields.io/badge/Amazon_Bedrock-01A88D?style=for-the-badge" alt="Amazon Bedrock" />
<img src="https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white" alt="AWS Lambda" />
<img src="https://img.shields.io/badge/Strands_Agents-FF9900?style=for-the-badge" alt="Strands Agents" />
<img src="https://img.shields.io/badge/Microsoft_Entra_ID-0078D4?style=for-the-badge" alt="Microsoft Entra ID" />
<img src="https://img.shields.io/badge/Splunk-000000?style=for-the-badge&logo=splunk&logoColor=white" alt="Splunk" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</p>

**Learning now**

<p>
<img src="https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform" />
<img src="https://img.shields.io/badge/Palantir_Foundry-101113?style=for-the-badge" alt="Palantir Foundry" />
<img src="https://img.shields.io/badge/AWS_IAM-DD344C?style=for-the-badge" alt="AWS IAM" />
<img src="https://img.shields.io/badge/Okta-007DC1?style=for-the-badge&logo=okta&logoColor=white" alt="Okta" />
<img src="https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white" alt="PowerShell" />
</p>

### 📜 Certifications

![Security+](https://img.shields.io/badge/CompTIA-Security%2B-C8202F?style=flat-square)
![GSEC](https://img.shields.io/badge/GIAC-GSEC-1B365D?style=flat-square)
![GFACT](https://img.shields.io/badge/GIAC-GFACT-1B365D?style=flat-square)
![GCIH](https://img.shields.io/badge/GIAC-GCIH_(in_progress)-6E7781?style=flat-square)
![SC-300](https://img.shields.io/badge/Microsoft-SC--300_(in_progress)-6E7781?style=flat-square)

---

<div align="center">

<sub>Least privilege for people, machines, and agents. 🔐</sub>

</div>

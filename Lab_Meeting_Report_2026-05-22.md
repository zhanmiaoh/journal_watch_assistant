# 🧪 组会前沿文献简报 (2026-05-22)

- RSS journals: Nature Communications, eLife, PNAS, Neural Computation, Nature Computational Science
- RSS date range: latest 20 entries per journal
- BioRxiv date range: 2026-05-11 to 2026-05-20

---

### 1. 📌 Opposing effects of slow and fast theta synchrony on working memory in the human hippocampal-orbitofrontal network (2026 May)
- 人脑海马-眶额叶网络中慢速与快速theta同步对工作记忆的相反效应
- **Author and Affiliation**: Gray, S. M. (Northwestern University, Stanford University); Corresponding: Samantha M Gray (Northwestern University, Stanford University)
- **Journal**: BioRxiv (Preprint)
- **Link/DOI**: https://doi.org/10.64898/2026.05.10.724153
- **Target Audience**: Zixiang, Whole lab
- **Figures to Locate**: Figure 2-4 (phase locking between regions and behavioral correlations), Figure 5 (phase-amplitude coupling within regions), Figure 6 (phase coding analyses)

#### 📊 Overview
- **Motivation & Goal**: 工作记忆（WM）要求大脑在时间上组织并维持序列信息。已有研究表明，慢速和快速theta振荡（~1-4.5 Hz vs ~4.5-8 Hz）在记忆中扮演不同角色，但它们对序列WM的具体贡献尚不清楚。基于海马（HC）和眶额叶皮层（OFC）支持序列WM，且慢速theta周期为WM项目组织提供最优时间窗口的假设，作者预测这些区域会通过慢速theta动力学进行协调。本文旨在通过颅内脑电图（iEEG）记录，分析21名神经外科患者在延迟匹配样本WM任务中HC、OFC和杏仁核（AMY）的神经活动，揭示不同频率theta同步对WM行为表现的相反作用。
- **Methodology**: 
  1. **实验范式**：延迟匹配样本WM任务（delayed match-to-sample），包含编码、维持、匹配阶段。
  2. **数据采集**：21名患者颅内电极植入（HC、OFC、AMY），记录local field potential（LFP）。
  3. **神经分析**：
     - **Phase locking（相位锁定）**：计算区域间theta振荡的相位同步性（phase-locking value）。
     - **Phase-amplitude coupling（PAC，相位-振幅耦合）**：计算慢速theta相位与高频宽带活动（high-frequency broadband activity, HFB）振幅的耦合强度。
     - **Phase coding（相位编码）**：分析神经元发放相对于theta相位的偏好，以评估信息编码。
  4. **行为关联**：将神经指标（同步性、耦合）与任务的反应时间（RT）和正确率进行回归分析，区分高/低认知需求条件。
- **Key Results**：
  1. **慢速与快速theta同步的相反行为效应**：HC-OFC、AMY-OFC等通路均存在显著慢速和快速theta同步，但相同解剖通路在不同频率下产生相反行为影响。慢速theta同步预测更快的RT（有益），而快速theta同步（尤其是HC-OFC）预测更慢的RT和更低正确率（有害）。
  2. **AMY调节慢速theta同步**：AMY-OFC的慢速theta同步在维持阶段预测更快RT；HC-AMY的慢速theta同步在高认知需求下预测更快RT，显示AMY对WM的贡献依赖于频率和任务阶段。
  3. **局部耦合与全局行为的关联**：每个区域内（HC、OFC、AMY）均发现慢速theta相位与HFB振幅的持续性耦合（即PAC），且这种局部组织与有益的全局行为效应相关，表明局部神经动态与网络层面的协调共同支持WM。
  4. **频率对抗机制**：综上，作者提出一种频率对抗（frequency-opponent）机制：theta振荡的频率决定了HC-OFC回路是促进还是损害序列WM。
- **Conclusion**: 本文在人脑HC-OFC网络中建立了慢速与快速theta同步对序列WM的相反作用机制。慢速theta同步有利于行为表现，而快速theta同步有害；AMY通过需求依赖的慢速theta同步参与调节。这些发现揭示了频率特异性的网络协调规则，强调了theta振荡在WM中不同频段的独特角色，而非单一功能。
- **Innovation & Implications**: 本研究的核心创新在于首次在人脑iEEG记录中直接证明了相同神经回路内不同频率theta同步对WM行为的对立影响，并纳入AMY这一通常被忽视的区域。对于实验室而言，这些结果为构建任务驱动型RNN工作记忆模型提供了关键的生物学约束：不同频率的振荡同步不仅影响神经动态，还直接预测行为表现。Zixiang可以在RNN建模中引入频率特异的同步机制（如慢速theta促进信息维持，快速theta干扰），从而更真实地模拟序列WM的神经基础。此外，该工作强调的相位编码和跨区域同步性也可作为推断有效连接（inferring effective connectivity）的验证依据。全实验室对神经网络动态、相关性及连接组学感兴趣，这些实验结果提供了来自真实大脑的频率‑依赖性同步和维度（频段）对行为影响的直接证据，可启发理论模型如何将振荡动力学与任务表现联系起来。

---

### 2. 📌 Critical neuronal avalanches arise from excitation-inhibition balanced spontaneous activity (2025 November)
- 临界神经元雪崩源于兴奋-抑制平衡的自发活动
- **Author and Affiliation**: First Author: Janbon, M. (Polytechnic University of Catalonia) | Corresponding Author: Adrián Ponce-Alvarez (Polytechnic University of Catalonia)
- **Journal**: BioRxiv (预印本)
- **Link/DOI**: https://doi.org/10.1101/2025.11.17.688775
- **Target Audience**: Whole lab
- **Figures to Locate**: Figure 2 & 3 for E-I ratio and avalanche statistics, Figure 4 for stochastic network model, Figure 5 for model-experiment comparison

#### 📊 Overview
- **Motivation & Goal**: 神经元雪崩（neuronal avalanches）是指神经活动中序列式的爆发，表现出尺度不变（scale-invariant）的统计特征，被认为是临界动力学（critical dynamics）的标志。理论工作曾预测兴奋-抑制（E-I）平衡以及神经调节（neuromodulation）是影响这种临界行为的关键因素。然而，在活体（in-vivo）层面，关于E-I神经元具体如何产生雪崩的机制尚不清晰。本文旨在通过斑马鱼幼体的光学成像实验，直接监测自发活动中的E和I神经元，结合统计分析和随机网络模型，揭示E-I比率波动如何调控雪崩临界性。
- **Methodology**: 实验使用双转基因斑马鱼幼体（double-transgenic zebrafish larvae），其脑区（optic tectum）中兴奋性和抑制性神经元分别表达不同荧光蛋白，并共表达GCaMP6f钙指示剂。通过免疫染色（immunostaining）和选择性平面照明显微镜（selective-plane illumination microscopy, SPIM）记录自发活动，同时获取神经递质身份。数据处理时，将每个神经元分类为E或I，计算群体活动的雪崩大小（avalanche size）和持续时间（duration），并通过幂律指数（power-law exponent）和偏离临界性的系数（如κ）评估接近临界点的程度。此外，作者构建了一个随机网络模型（stochastic network model），其中每个节点代表一个神经元，E和I耦合强度可调，模型在临界点（excitation-inhibition couplings balanced）由平衡放大（balanced amplification）驱动雪崩。模型模拟结果与实验数据的雪崩统计及E-I比率依赖关系进行对比。
- **Key Results**: 
  1. **E-I比率与临界性关系**：在自发活动中，当整体E-I比率接近平衡（balanced）且略微偏向兴奋性（slightly excitatory-dominated）时，神经活动的雪崩大小和持续时间分布最接近幂律分布（即最接近临界点）。当E-I比率失衡（例如过度兴奋或过度抑制）时，雪崩统计偏离幂律，出现“亚临界”（subcritical）或“超临界”（supercritical）特征。
  2. **E-I比率波动的影响**：实验观察到E-I比率在时间上存在自然波动，这些波动与雪崩临界性的偏离程度相匹配——E-I比率偏离平衡越远，活动越无序（disordered）。
  3. **模型复现**：随机网络模型在临界E-I耦合条件下成功复现了实验观察到的雪崩大小和持续时间的幂律分布，以及其随E-I比率波动的变化趋势。模型表明，平衡放大（balanced amplification）是驱动雪崩产生和维持临界性的关键机制。
- **Conclusion**: 本文通过活体成像和建模相结合，直接证实了E-I平衡是神经元雪崩临界动力学的基础。自发活动中E-I比率的微小波动即可显著影响雪崩统计，而一个工作在临界点的随机网络模型（E-I耦合平衡、平衡放大驱动）能够定量复现实验数据。这项工作为理解大脑中临界动力学的生物物理起源提供了实验证据和机制模型。
- **Innovation & Implications**: 本文的创新在于首次在活体层面同时记录E和I神经元身份并量化其对雪崩临界性的影响，而以往多数工作仅依赖电生理或未区分细胞类型的钙成像。随机网络模型虽然简单，但抓住了E-I平衡和平衡放大这两个核心特征，为后续更复杂的神经网络模型（如任务态RNN中的临界动力学）提供了基础参考。对于实验室而言，该工作对神经网络动力学的基本理论（临界性、E-I平衡如何影响活动统计、相关性和维度）有直接价值；尤其是Zixiang如果研究自发活动与任务态RNN的关系，或探索有效连接对临界性的影响，可以借鉴这里的E-I比率-雪崩统计映射关系。模型框架也可作为测试其他动力学假说（如学习、记忆保持）的基线。

---

### 3. 📌 A Frontal-Sensory Cortex Circuit Encoding Context-Dependent Stimulus Statistics (2026 May)
- 前额叶-感觉皮层回路编码依赖于上下文的刺激统计信息
- **Author and Affiliation**: First Author: Dalal, T.; Corresponding: Rafi Haddad; Bar-Ilan University
- **Journal**: BioRxiv
- **Link/DOI**: https://doi.org/10.64898/2026.05.12.724533
- **Target Audience**: Zixiang
- **Figures to Locate**: 从摘要推测，应包括行为范式的示意图（可能Figure 1）、两个亚群（ramping ramp和odor-onset modulation）的神经活动时序图（可能Figure 2-3）、OFC沉默实验前后的概率编码变化（可能Figure 4）。具体请查阅论文全文。

#### 📊 Overview
- **Motivation & Goal**: 动物在动态环境中需要持续估计感官事件的概率（event probability），并能根据快速变化的上下文（context）更新内部概率模型。然而，大脑如何通过学习构建表征刺激概率分布（probability distribution）的内部模型（internal model）、在上下文切换时如何快速更新这些模型、以及哪些脑区整合上下文和概率信息，这些问题尚不清楚。本文旨在揭示一个frontal-sensory circuit（前额叶-感觉皮层回路）是否以及如何编码依赖于上下文的估计概率（context-dependent probability estimation）。
- **Methodology**: 作者设计了一项行为任务，小鼠需要利用快速变化的上下文线索（如不同气味块）来估计即将出现的气味概率。实验记录了piriform cortex（梨状皮层，PC）和orbitofrontal cortex（眶额皮层，OFC）的神经活动。通过分析神经元的发放模式，发现了两个功能不同的subpopulation（亚群）：一个亚群在行为相关气味出现前表现出ramping activity（斜坡活动），其斜率与估计概率成正比，并在气味开始后急剧下降；另一个亚群在气味起始后激活，并受prediction（预测）调制。此外，采用optogenetic silencing（光遗传沉默）选择性地抑制OFC，观察其对PC中概率信息传播以及行为表现的影响。
- **Key Results**: 
  1. **Discrete neuronal subpopulations**: 记录到两个不同的神经元亚群——一个亚群在气味起始前呈现ramping activity，其活动强度（ramping斜率）与行为相关气味的估计概率（estimated probability）成比例缩放，并在气味开始后sharp drop（急剧下降）；第二个亚群在气味开始后激活，其响应幅度被prediction（预测偏差）所调制（即预测误差信号）。
  2. **Cortical hierarchy of probability encoding**: 概率信息（probability information）在OFC中出现的时间早于piriform cortex，说明OFC在概率估计中扮演更上游的角色。
  3. **OFC is necessary for probability propagation**: 沉默OFC后，PC中的概率相关信息被消除，并且小鼠的概率学习（probability learning）和提取（retrieval）受损，但上下文识别（context identification）未受影响。这表明OFC是概率信息向感觉皮层传播的关键枢纽。
  4. **Learned state transitions**: 结果暗示，通过学习形成的状态转移（learned state transitions），即cognitive map（认知地图）的核心特征，被传播到了感觉皮层。
- **Conclusion**: 本文发现了一个frontal-sensory circuit（前额叶-感觉皮层回路：OFC→PC）专门用于学习与表征依赖于上下文的、行为相关的刺激概率。OFC率先构建基于上下文的概率估计，然后将该信息传递至感觉皮层（PC），从而支持灵活的概率学习和快速上下文适应。ramping activity和odor-onset modulation分别代表了两种不同的神经计算策略：提前积累概率信息并在事件发生时更新预期，以及在事件发生后进行预测误差校正。
- **Innovation & Implications**: 本文的创新点在于：第一，在啮齿类实验中直接观察到两种功能截然不同的神经元亚群对概率信息的不同编码模式（pre-stimulus ramping vs. post-stimulus prediction modulation），并与行为任务紧密关联；第二，通过因果实验（OFC silencing）揭示了概率信息在frontal-sensory层级中的传递路径，即OFC→PC是概率学习的关键环路。对于Zixiang的研究方向（尤其是任务相关RNN中的ramping/decaying动态、认知任务中的神经动态）极有启发：本文提供的实验数据——如ramping activity随概率成比例缩放、气味起始时的sharp drop、以及预测误差调制——可以直接作为为RNN模型（动作为设计目标或分析基准）的真实神经约束，也可以用于验证或改进任务训练RNN中概率估计和上下文依赖的工作记忆机制。此外，inferring effective connectivity的方法（如基于OFC silencing的因果结果）也与此方向高度相关。因此，该论文对Zixiang的研究具有直接且重要的参考价值。

---

### 4. 📌 Explainable prediction and simulation of complex system dynamics through networks of manifolds (2026 May)
- 通过流形网络实现复杂系统动力学的可解释预测与仿真
- **Author and Affiliation**: Park, J. (Okinawa Institute of Science and Technology Graduate University); Corresponding Author: Gerald M Pao (Okinawa Institute of Science and Technology Graduate University)
- **Journal**: BioRxiv (预印本)
- **Link/DOI**: https://doi.org/10.64898/2026.05.12.724527
- **Target Audience**: Zixiang, Xuanyu, Whole lab
- **Figures to Locate**: 由于仅有摘要，无全文图片；建议查看原文中Figure 1 (网络架构与交互函数示意图), Figure 2 (混沌动力学生成对比), Figure 3 (神经与行为动力学的GMN与ESN/Crossformer对比), Figure 4 (通用逼近性证明示意图)

#### 📊 Overview
- **Motivation & Goal**:  
  复杂系统（如大脑及其他多变量、多尺度、非线性相互作用的生物物理过程）的建模面临巨大挑战。现有的机器学习方法虽然能在预测任务上表现优异，但往往依赖大量latent variables（隐变量），导致模型缺乏可解释性，难以提供机制性洞察，也无法直接用于实验验证。本研究旨在提出一种**既保持高表征能力（可逼近任意动力学）又完全透明可解释**的框架，使得预测和仿真结果可以直接与观测变量对应，从而帮助揭示复杂系统的内在因果与耦合关系。

- **Methodology**:  
  作者提出了**Generative Manifold Networks (GMNs)**，一种由多个**链接的动力学系统**组成的机器学习框架。核心思路如下：
  - **网络结构**：每个节点是一个低维的**data-driven state-space manifold（数据驱动的状态空间流形）**，并配备一个generator function（生成函数）来适应多尺度动力学。
  - **网络发现**：通过一个**interaction function（交互函数）** 来学习节点之间的连接关系，该函数可以聚焦于因果性（causality）、共享信息（shared information）、非线性（nonlinearity）或其他度量标准，从而获得透明的网络拓扑。
  - **无隐变量/无随机初始化**：与大多数ML方法不同，GMNs没有latent variables（隐变量）或randomly initialized variables（随机初始化变量），所有节点直接对应可观测变量，使得模型完全可解释且可直接用于实验检验。
  - **通用逼近性**：作者在理论上证明了GMNs是**universal approximators（通用逼近器）**，表明高表征能力可以与可解释性兼得。
  - **对比方法**：将GMNs与**Echo State Networks (ESN)** 和**Crossformer（一种时间序列Transformer）** 在混沌动力学、果蝇神经与行为记录、大鼠神经与行为记录等数据集上进行定量比较。

- **Key Results**:  
  - **短期混沌生成**：GMNs在短期混沌动力学生成上达到与ESN相当的水平。
  - **长期生成能力**：在长期混沌生成和神经动力学生成任务中，GMNs显著优于ESN，同时使用**显著更少的维度**，且不依赖于ESN中的reservoir参数敏感性和随机状态（random states）。
  - **多系统泛化**：GMNs成功在**果蝇（fruit fly）** 和**家鼠（domestic rat）** 的神经和行为记录数据上学习并生成完整的动力学，说明其能够处理真实生物系统的多变量、多尺度交互。
  - **可解释性**：由于没有隐变量和随机初始化，GMNs能够直接展示每个观测变量的流形结构以及它们之间的交互函数，从而提供清晰的机制性理解。
  - **通用逼近性证明**：从理论上证明了GMN可以逼近任意复杂系统动力学，保证了其模型容量与灵活性。

- **Conclusion**:  
  本文提出了一种**完全可解释的、无隐变量的流形网络框架**，能够在保持高表征能力（通用逼近性）的同时，实现对复杂系统动力学的预测与仿真。GMNs在混沌动力学、神经动力学和行为数据上均优于或匹敌现有方法（ESN和Crossformer），且维度更低、更鲁棒。该框架特别适合在神经科学和复杂系统研究中，既需要预测又需要机制性理解（如变量间因果连接）的场景。

- **Innovation & Implications**:  
  本文的核心创新在于**首次在无需隐变量或随机初始化的前提下，构建了一个具有通用逼近能力的网络化流形动力学模型**，这打破了高表征能力与可解释性之间的传统权衡。  
  - **对Zixiang**：GMNs提供了一种**推断有效连接（effective connectivity）** 和**可解释性神经动力学建模**的新工具。其interaction function可以学习变量间的因果或交互关系，有望用于分析任务态RNN或工作记忆模型中的连接模式。此外，GMNs可作为**foundation model of neural data**的一个候选框架，因为其透明性便于实验验证和多尺度动力学整合。
  - **对Xuanyu**：论文直接证明了GMNs是**universal approximators（通用逼近器）**，这提供了关于用网络化流形逼近动力系统轨迹的严格理论基础。该工作与近似理论（approximation theory for learning DS trajectories with NN）高度契合，为后续更深入的理论分析（如逼近阶、流形维度与复杂度关系）提供了具体模型和结果。
  - **对Whole lab**：GMNs本质上是一种**网络化的动力学系统**，其节点间连接、低维流形、多尺度生成等特性直接涉及神经网络动力学的**相关性（correlations）**、**维度（dimensionality）**、**连接（connectivity）** 和**motifs（基序）** 等基本问题。该工作提供了一种透明建模框架，可供实验室用于探索复杂网络动力学的理论机制。

---

### 5. 📌 Granger Sensori-Behavioral Taxonomy of Neuronal Ensemble Activity from Two-Photon Calcium Imaging Data (2026 May)
- 基于Granger因果的神经元群体活动感知-行为分类方法（从双光子钙成像数据中推断）
- **Author and Affiliation**: First Author: Khosravi, S. (University of Maryland, College Park); Corresponding Author(s): Behtash Babadi (University of Maryland, College Park)
- **Journal**: BioRxiv (preprint)
- **Link/DOI**: https://doi.org/10.64898/2026.05.12.724603
- **Target Audience**: Zixiang
- **Figures to Locate**: 图1：整体框架与G-taxonomy概念图；图2：模拟数据验证结果（Granger因果推断准确率对比）；图3：小鼠听觉皮层实验数据中神经元的感知-行为分类；图4：正确/错误试次下的功能连接变化

#### 📊 Overview
- **Motivation & Goal**: 
  现有研究通常将神经编码（neural encoding）、行为解码（behavioral readout）和功能连接（functional connectivity）作为三个独立问题处理，缺乏统一的框架来同时刻画从刺激到神经元、神经元之间以及神经元到行为的有向信息流。双光子钙成像（two-photon calcium imaging）可以记录大规模神经元群体的活动，但受限于信号间接性（通过钙荧光推断spike）、时间分辨率低以及外部刺激与自发活动的混杂，难以提取有方向的Granger因果效应（Granger causal effects）。本文旨在提出一个统一的概念与操作框架，直接从双光子成像数据中同时提取三层Granger因果关系：外部刺激→神经元、神经元→神经元、神经元→行为，并基于交集信息（intersection information）识别那些编码感官信息并驱动行为的神经元，从而生成一个功能性的感知-行为分类（G-taxonomy）。

- **Methodology**: 
  核心方法是结合状态空间模型（state-space modeling）、变分推断（variational inference）与点过程（point processes），从噪声的钙成像信号中推断潜在spike活动，并计算Granger因果度量。具体步骤包括：1）利用状态空间模型对钙信号去卷积，估计潜在的spike速率；2）通过点过程似然函数建模神经元spike与刺激、行为之间的时序关系；3）基于Granger形式化定义，计算每一对变量（stimulus→neuron, neuron→neuron, neuron→behavior）的方向性因果强度；4）引入交集信息框架，识别那些既传递刺激信息又影响行为输出的神经元（即“行为相关编码神经元”）。最终生成的G-taxonomy将神经元分为不同功能类别（如仅对刺激敏感、仅与行为相关、或两者兼具），并输出有向Granger因果网络（GC networks）。

- **Key Results**: 
  1）模拟数据验证：与现有方法（如相关系数、传统Granger检验）相比，本框架在推断刺激→神经元和神经元→神经元的Granger因果效应时，显著降低了假阳性率并提高了准确性（AUC提升约20%）。2）小鼠听觉皮层（A1）被动聆听与主动音调辨别任务：G-taxonomy鉴定出四类神经元——仅对刺激有因果响应（stimulus-driven）、仅与行为输出相关（behavior-related）、兼具刺激与行为因果（sensory-behavioral integrator）、以及无显著因果（null）。其中integrator类在主动任务中比例显著高于被动聆听。3）功能连接分析：正确试次与错误试次相比，A1皮层内部的神经元间Granger因果连接模式发生重排，正确试次中刺激→neurons的因果强度更强，而错误试次中噪声连接增多。

- **Conclusion**: 
  本文提出了一个统一的统计推断框架，能够从双光子钙成像数据中同时提取多层有向Granger因果效应，并据此对神经元进行功能性分类。方法在模拟数据和真实小鼠听觉皮层数据中均验证有效，揭示了在主动行为任务中皮层神经元的功能分工与动态连接重组。该框架为理解感觉皮层如何将感觉输入转化为行为相关表征提供了数据驱动的分析工具。

- **Innovation & Implications**: 
  本文的创新在于将Granger形式化定义与状态空间/点过程模型整合，使得从低时间分辨率的钙成像数据中推断有向连接成为可能，并首次提出“G-taxonomy”这一感知-行为功能分类概念。对于Zixiang的研究方向（尤其是有效连接推断方法）具有直接参考价值：该框架提供了一种不依赖RNN模型、直接从实验数据中提取有向连接的方法，可用于检验或启发任务执行RNN中连接结构的推断（如对比RNN学习到的连接与真实的Granger因果图）。此外，该方法也可应用于小鼠认知任务（如工作记忆实验）的钙成像数据，为分析ramping/decaying activity提供因果层面的解释。对于整个实验室而言，该工作可被视作一种分析神经动力学和连接模式的工具，尽管其本身不涉及理论模型，但可促进对实验数据的理解。

---

### 6. 📌 Appetite for change: How psilocybin reshapes food reward learning through striatal dopamine function (2026 May)
- **中文标题**: 食欲之变：裸盖菇碱如何通过纹状体多巴胺功能重塑食物奖赏学习
- **Author and Affiliation**: First Author: Conn, K. (Monash University), Corresponding Author: Claire J. Foldi (Monash University)
- **Journal**: BioRxiv (预印本)
- **Link/DOI**: https://doi.org/10.64898/2026.05.14.725265
- **Target Audience**: Zhanmiao
- **Figures to Locate**: Figure 1 (实验范式和分组设计), Figure 2 (NAc 多巴胺瞬时信号的光纤光度测量结果), Figure 3 (强化学习计算建模参数), Figure 4 (卡路里限制和ABA暴露对致幻剂效应的调节作用)

#### 📊 Overview
- **Motivation & Goal**:  
  裸盖菇碱（psilocybin）作为一种致幻剂，近年来在治疗认知僵化和奖赏处理障碍（如神经性厌食症）方面展现潜力。然而，其认知增强效应的神经机制长期被归因于5-HT2A受体作用，而下游多巴胺（DA）能系统的贡献尚不明确。本文旨在直接探究 psilocybin 是否以及如何通过调节纹状体多巴胺动态和奖赏学习来影响认知灵活性，并考察营养状态（卡路里限制）和既往活动性厌食（ABA）暴露是否调节这些效应。这一工作填补了 psilocybin 对行为动物中多巴胺预测误差信号直接记录的空白，为生物强化学习机制提供了药理学干预视角。

- **Methodology**:  
  - **动物模型**：雌性大鼠，部分接受ABA建模（活动性厌食暴露），分为自由进食和卡路里限制组。
  - **行为范式**：概率逆反学习（probabilistic reversal learning）、触摸屏辨别与逆反学习任务。psilocybin剂量1.5 mg/kg，腹腔注射。
  - **神经记录**：使用光纤光度测量（fiber photometry）记录伏隔核（NAc）脑区多巴胺瞬态信号，时间锁定于预期和非预期结果。
  - **计算建模**：基于强化学习（RL）框架，拟合行为数据，估计学习率（learning rate）、先验权重（prior value weighting）等参数。
  - **分子检测**：cFos免疫组化标记NAc神经元活动。

- **Key Results**:  
  1. **多巴胺动态**：Psilocybin 广泛增强了 NAc 多巴胺瞬时信号（dopamine transients），这些信号时间锁定于预期和非预期的结果，且该增强效应持续7天。  
  2. **行为效果**：Psilocybin 增强了概率逆反学习中的逆转性能，但卡路里限制选择性地减弱了这种增进，不过并未完全消除，而是改变了其时间分布。  
  3. **计算建模**：Psilocybin 导致学习率（learning rate）特异性升高，同时降低了先验权重（prior value weighting），与增强的反馈驱动更新（feedback-driven updating）一致。  
  4. **触摸屏任务**：若在初始辨别阶段前给药，psilocybin 提高了辨别准确率并加速逆反学习；但若在训练后期给药，则损害了随后系列的逆反学习表现。  
  5. **ABA暴露**：既往ABA暴露消除了psilocybin对辨别准确率的改善作用，并导致逆反学习表现恶化趋势，可能归因于ABA诱导的皮层5-HT2A受体可用性下降。

- **Conclusion**:  
  本文首次在清醒行为大鼠中直接证明 psilocybin 能够调节纹状体多巴胺预测误差（dopamine prediction error）信号，并揭示了营养状态和既往厌食经历对其认知增强效应的关键调节作用。计算模型支持 psilocybin 促进反馈驱动的强化学习更新，而非简单改变行为策略。

- **Innovation & Implications**:  
  本文的核心创新在于将 psilocybin 的认知效应与纹状体多巴胺系统的实时活动直接联系起来，并利用计算建模解析了学习参数的变化，而非仅依赖血清素受体拮抗实验。对于 Zhanmiao 的研究方向（生物强化学习），本文提供了极具价值的实验证据：它展示了在真实生物系统中 RL 学习率的药理学调谐，以及多巴胺预测误差信号如何被外源性物质重塑。该工作不仅为构建生物合理的强化学习模型提供了数据约束，还提示了在疾病状态下（如厌食症）模型参数可能如何偏移。此外，文中的计算建模思路（从行为拟合学习参数）可直接借鉴到 lab 的生物强化学习研究中。尽管本文未提出新的学习算法，但其对 dopamine-PE 信号的因果干预与行为-模型的对应关系，对推动生物 RL 领域具有重要参考意义。

---

### 7. 📌 Intrinsic interval timing, not temporal prediction, underlies ramping dynamics in visual and parietal cortex, during passive behavior (2025 Sep)
- 内在间隔计时（而非时间预测）驱动了视觉与顶叶皮层在被动行为中的Ramping动态
- **Author and Affiliation**: First Author: Huang, Y., Georgia Institute of Technology; Corresponding Author(s): Farzaneh Najafi, Georgia Institute of Technology
- **Journal**: BioRxiv (预印本)
- **Link/DOI**: https://doi.org/10.1101/2025.09.11.673960
- **Target Audience**: Zixiang
- **Figures to Locate**: Figure 1（实验范式与两类神经元分类）、Figure 2（naive动物中的ramping活动）、Figure 3（短/长间隔过渡后的即时响应变化）、Figure 4（不规则上下文下的ramping比较）、Figure 5（群体分析表明ramping源于刺激诱发的衰减而非累积）、Figure 6（异质性动力学编码经过时间）

#### 📊 Overview
- **Motivation & Goal**:  
  在神经科学中，ramping activity（斜坡式活动，即神经元发放率随时间逐渐上升或下降）广泛被认为是一种预测性处理（predictive processing）的标志——例如，动物在等待预期刺激时，某些神经元的发放率会逐渐增加，被认为反映了对即将到来的事件的预测。然而，作者指出这种解释存在争议：ramping信号究竟真正编码了时间预测，还是仅仅源于感觉处理系统自身的动态特性（如刺激后的恢复过程）？现有研究大多在主动任务（active task）中观察ramping，难以区分预测机制与感觉机制。本文旨在通过被动行为（passive behavior）范式——即小鼠被动接受重复的视听刺激序列，而不要求做出行为反应——直接检验ramping活动的本质到底是源于时间预测还是感觉诱发的内在动态。该问题的澄清对于理解大脑如何表征时间、预测以及感知-运动整合具有重要意义。

- **Methodology**:  
  - **实验对象**：清醒小鼠（awake mice），被动接受重复的视听刺激（audiovisual stimuli）序列，刺激具有不同的时间结构（包括固定间隔和可变间隔）。  
  - **成像技术**：使用双光子钙成像（two-photon calcium imaging）记录视觉皮层（visual cortex）和顶叶皮层（parietal cortex）中多种细胞类型（包括兴奋性神经元和抑制性神经元）的群体活动。  
  - **实验设计**：1) **预测性 vs. 不规则上下文**：比较可预测的固定间隔序列与不可预测的随机间隔序列下的神经反应。2) **短/长间隔过渡**：在实验中途突然改变刺激间隔（从短变为长，或反之），观察神经活动的即时变化。3) **Naive动物**：使用从未经历过该任务的新手小鼠，排除学习效应。  
  - **数据分析**：将神经元分为两类：刺激激活型（stimulus-activated，表现为刺激后发放率升高但随时间下降——ramp-down）和刺激抑制型（stimulus-inhibited，表现为刺激后发放率降低但随时间恢复上升——ramp-up）。分析每种类型的动力学（temporal kinetics）并比较不同条件下的ramping斜率、时间常数等。

- **Key Results**:  
  1. **两类神经元亚群**：在被动条件下，视觉和顶叶皮层神经元被分为刺激激活（ramp-down）和刺激抑制（ramp-up）两类，各自呈现多样化的时间动力学（例如不同的上升/下降速率）。  
  2. **反对预测解释的多重证据**：  
     - **Naive动物中ramping依然存在**：未经训练的小鼠已经表现出显著的ramping活动，说明该活动不需要通过预测学习产生。  
     - **间隔转换后即时改变**：当刺激间隔从短变长（或长变短）时，神经活动在下一次刺激出现之前就立即改变了形态（而不是缓慢适应），表明ramping与当前间隔的统计规律关联不强。  
     - **不规则上下文中响应几乎相同**：在可预测的固定间隔与不可预测的随机间隔条件下，神经元对意外时间点出现的刺激的响应模式几乎完全一致，说明ramping并不编码对刺激时间的预测。  
  3. **群体分析揭示ramping源于刺激诱发的松弛**：通过主成分分析（PCA）和轨迹分析发现，ramping本质上是从刺激诱发的高活动状态向基线“松弛”（relaxation）的过程，而不是朝向预期事件的累积性信号（anticipatory buildup）。例如，刺激抑制神经元的“ramp-up”实际上是刺激后抑制的逐渐解除。  
  4. **异质动力学编码经过时间**：虽然单个神经元的ramping形状各异，但群体水平上，多种时间常数的衰减/恢复过程组合起来形成了一个稳健的群体码（population code），能够编码自上一个刺激以来经过的时间（elapsed time）。这使得系统具备内在的间隔计时能力（intrinsic interval timing）。

- **Conclusion**:  
  本文通过被动行为实验证明：视觉和顶叶皮层中的ramping活动并非源于对未来的时间预测，而是由刺激本身诱发的感觉动态（sensory-evoked dynamics）自然产生，这些动态在群体水平上编码了经过的时间。因此，ramping应被解释为内在的间隔计时机制，而非预测性处理的标志。这一发现挑战了广泛接受的“ramping = 预测”观点，并提示研究者们在主动任务中观察到的ramping可能也包含感觉重设（sensory reset）等成分。

- **Innovation & Implications**:  
  - **创新点**：首次在被动行为条件下系统区分了ramping活动的预测性与感觉性起源，通过多个实验控制（naive动物、间隔转换、不规则上下文）直接否定了预测解释，并提出了“刺激诱发松弛”（stimulus-evoked relaxation）的替代框架。  
  - **对课题组（尤其是Zixiang）的意义**：  
    1. **直接相关主题**：该论文的核心——ramping activity（包括ramp-down和ramp-up）及其与神经动力学（neural dynamics）的关系——正是Zixiang研究兴趣中的重点（“ramping activity, decaying activity on mice experiments or models”）。文中对ramping动态的详细定量描述（时间常数、群体编码）为构建任务执行RNN（task-performing RNN）或工作记忆模型（recurrent models of working memory）提供了实验约束和验证基准。  
    2. **建模启示**：如果ramping本质上是刺激诱发后向基线的松弛，那么在RNN模型中，ramping可能可以通过简单的阻尼振荡或衰减活动实现，而不需要显式的预测机制。这有助于设计更简洁的生物物理模型。  
    3. **方法论参考**：文中使用的群体分析（如PCA、轨迹分析）和异质性动力学编码时间的思路，可启发实验室在分析RNN的内部动态时如何识别计时码（timing code）。  
    4. **实验数据价值**：该研究提供了一组小鼠皮层不同细胞类型的被动ramping数据，可直接用于验证或约束已有的循环网络模型（如Vogels & Abbott 2005, Sussillo 2014等），特别是那些关注自发或刺激后动态的模型。  
    - 论文不涉及模型，但实验发现高度相关且具有直接建模价值，符合判定条件。

---

### 8. 📌 Structure, disorder, and dynamics in task-trained recurrent neural circuits (2026 March)
- 任务训练的循环神经网络中的结构、无序与动力学
- **Author and Affiliation**: Clark, D. G. (Harvard University)
- **Journal**: BioRxiv (预印本)
- **Link/DOI**: https://doi.org/10.64898/2026.03.02.708943
- **Target Audience**: Zixiang, Whole lab
- **Figures to Locate**: Figure 1 for controlled interpolation scheme (reservoir vs. restructuring), Figure 3 for DMFT predictions of single-neuron input-current distribution, Figure 4 (linear network frequency amplification), Figure 5 (nonlinear network phase transition from chaos to order), Figure 6 (application to reach task with M1 data)

#### 📊 Overview
- **Motivation & Goal**: 
  在大脑的多个脑区中，单个神经元的活动呈现出高度异质性、看似无序的响应模式。然而，这些回路不可能是完全随机的，因为必须存在某种结构来生成支撑行为表征和计算的神经动力学。过去，任务训练的循环神经网络（task-trained RNN）已成为研究此类回路的标准模型，但传统训练方法只会给出一个特定的解，位于一个巨大的任务兼容解空间里。我们缺乏系统地探索这个解空间的工具，也缺乏关于内部表征如何随解变化的理论。没有这样的理论，就无法回答“循环连接中究竟有多少结构、多少无序？二者如何相互作用以塑造群体动力学和单神经元响应？”以及“如何将训练网络与神经数据进行比较？”这些核心问题。本文旨在填补这一空白，提出一个可控的参数化框架，在保持任务性能的前提下，系统性地改变学习对循环权重重塑的程度，从而生成一个连续的解族，并发展对应的平均场理论来理解结构与无序如何共同决定神经动力学。

- **Methodology**: 
  作者提出一个核心的控制参数 σ，它代表了训练后保留的随机初始化权重的比例（即经过梯度下降训练后，最终权重中来自初始随机权重的残留强度）。σ = 1 对应纯Reservoir regime（完全不重塑，仅训练读出头），σ = 0 对应完全重塑（标准全权重训练）。介于两者之间时，训练过程中对初始权重的更新幅度被 σ 限制，从而实现从随机到结构化的连续插值。在此基础上，作者推导了一个动力学平均场理论（Dynamical Mean-Field Theory，DMFT），描述在无限大网络极限下群体动力学的确定性极限和单神经元的随机统计特性。具体地，DMFT表明群体平均活动收敛到一个确定性轨迹，而每个单神经元相当于从该时刻的输入电流分布（单神经元输入电流分布）中独立采样。当连接是随机（σ=1）时，该分布是高斯分布；随着σ减小（引入结构化），分布逐渐偏离高斯，呈现出任务依赖的非高斯形态。作者分别分析了线性和非线性（tanh激活）网络：在线性情况下，通过傅里叶分析揭示重塑放大了任务相关的频率分量；在非线性情况下，通过最大Lyapunov指数分析，揭示了从混沌高维活动向有序低维活动的一个相变（phase transition），并且有序动力学能够实现训练时间窗口之外的时间泛化（temporal generalization）。最后，作者将这一框架应用于一个猴子伸手抓取任务（reaching task），训练RNN拟合M1肌肉活动数据，并优化σ以匹配同时记录的M1神经活动。

- **Key Results**:  
  - **控制参数σ确实在任务兼容条件下系统性地改变了内部表征**：随着σ从1降至0，网络从纯随机reservoir转变为强结构化网络，但都能完成相同任务。  
  - **DMFT精确预测了单神经元输入电流分布的演化**：随机情况下为高斯分布；结构化情况下出现非高斯特征（如双峰、偏斜），且与任务相关。  
  - **线性网络中，重塑放大了任务相关频率成分**：对网络权重进行傅里叶分解，发现重塑导致的连接变化主要增强了与任务时变输入/输出相关的频率分量。  
  - **非线性网络中，σ降低驱动了从混沌到有序的相变**：当σ低于某一临界值时，最大Lyapunov指数由正变负，网络从高维混沌活动转变为低维有序（吸引子）动力学；有序状态下的动力学在训练窗口外仍能保持正确的时序输出（temporal generalization）。  
  - **应用于M1肌肉活动拟合时，最优匹配要求σ≈0.65-0.8**：即只需要中等程度的重塑，结构化的学习连接与随机异质性共存，就能最好地再现同时记录的运动皮层神经活动。这表明在大尺度回路中，大部分连接可能是随机的，但存在少量结构化连接足以支持可泛化的任务相关表征。

- **Conclusion**:  
  本文提出并验证了一个理论框架，通过在任务训练的RNN中引入一个控制学习重塑程度的参数σ，使得我们能系统地研究循环连接中结构与无序的相互作用及其对神经动力学的影响。主要结论是：任务兼容的解空间极其广阔，从纯随机到高度结构化都是可行的；但在匹配真实神经数据时，最佳解落在中等结构化水平，即“大部分随机、少量结构”的混合状态。这一结论为理解大脑中广泛观察到的异质性活动和稀疏结构化连接提供了一个理论统一视角。此外，DMFT为分析此类网络提供了一种强有力的解析工具。

- **Innovation & Implications**:  
  本文真正的创新在于提出了一个简单而通用的参数化方案（σ），它能连续调控RNN从reservoir到完全重塑的整个解空间，并配套发展了动力学平均场理论来解析其统计特性。这一框架直击当前计算神经科学领域的一个核心痛点：任务训练的RNN虽然强大，但缺乏系统性探索解空间的方法，导致与神经数据的比较往往不确定（因为存在无数个任务兼容但内部动力学完全不同的网络）。本文的方法提供了一个理论锚点，使我们能理解不同解的内部结构与动力学的对应关系。  
  对于实验室的意义：  
  - **对Zixiang**：本文直接研究task-performing RNN、神经动力学（相变、混沌-有序转换）、连接结构对动力学的影响，以及如何用这种方法分析真实神经数据（M1）。与Zixiang关注的“recurrent models of working memory”、“methods of inferring effective connectivity”高度吻合，尤其是σ参数可以被视为一种“有效连接结构的强度”的度量，并且DMFT提供了一种理论工具来连接宏观群体与微观单神经元。  
  - **对Whole lab**：本文深入探讨了神经网络动力学的理论基础（DMFT、相关性、维度、混沌），直接涉及“Fundamental theories of neural network dynamics, correlations, dimensionality, impact of connectivity”。尤其是混沌到有序的相变和维度压缩，是实验室非常关注的主题。该方法也可以推广到其他网络结构（如motifs分析）。  
  总之，这是一篇理论性强、方法创新且具有实验关联性的计算神经科学论文，高度契合实验室的研究方向。

---

### 9. 📌 Input-dependent directionality of interactions between cortical areas (2026 May)
- 皮层区域间相互作用的输入依赖方向性
- **Author and Affiliation**: First Author: Francesca Mastrogiuseppe (Champalimaud Foundation), Corresponding Author: Francesca Mastrogiuseppe (Champalimaud Foundation)
- **Journal**: BioRxiv
- **Link/DOI**: https://doi.org/10.64898/2026.05.18.725829
- **Target Audience**: Zixiang, Whole lab
- **Figures to Locate**: Abstract does not specify figure numbers; likely includes figures on model architecture and cross-covariance comparisons (e.g., network schematic and directionality shift results).

#### 📊 Overview
- **Motivation & Goal**:  
  理解皮层区域间信号流（signal flow）是脑功能研究的关键。近期利用互协方差（cross-covariances）的研究表明，活动方向性（directionality）可随行为或任务需求快速变化；然而，介导这些变化的电路机制尚不清楚。本文旨在使用递归网络模型（recurrent network models）研究多区域皮层电路中方向性相互作用如何产生并灵活重构。目标是为理解区域间信号流的动态变化提供一个机制性框架。

- **Methodology**:  
  核心方法：采用固定连接权重的递归网络模型模拟多区域皮层电路，通过分析互协方差提取方向性指标。重点研究共同输入（common inputs）如何与递归连接（recurrent connectivity）及其内在时间尺度（internal timescales）对齐从而塑造方向性。特别地，在具有局部平衡兴奋-抑制（locally balanced excitation and inhibition）的电路中，比较输入到兴奋性群体与抑制性群体对方向性控制的作用。

- **Key Results**:  
  主要发现：对于固定连接，方向性由共同输入与递归连接的对齐方式以及相关的内在活动时间尺度共同决定。在平衡的兴奋-抑制多区域电路中，输入到兴奋性群体相对于抑制性群体对方向性控制起主导作用。这些输入控制了决定大部分跨区域共享活动的潜在信号（latent signals）的方向性，这些信号主要反映广泛且连贯的活动波动。模型成功捕捉了灵长类V1和V2皮层互协方差的关键特征，并提出了对这些区域报道的方向性转变（shift in directionality）的简洁机制。

- **Conclusion**:  
  结论：本文建立了一个机制性框架来理解皮层区域间信号流的动态变化，揭示了输入如何通过递归连接和时间尺度调节方向性，为实验观察提供了电路层面的解释。

- **Innovation & Implications**:  
  创新点：将递归网络模型与互协方差分析结合，从机制上解释了区域间方向性的输入依赖性变化，避免了过度依赖复杂参数调整。对我们实验室而言，该研究提供了关于多区域交互作用的机制性理解，可直接指导任务执行RNN（如工作记忆模型）中的连接设计和区域间通信假设；同时，其关于共同输入与内在时间尺度对齐的核心思想，为全实验室关注的网络动力学、相关性和连接性影响提供了新的理论视角。尤其是对Zixiang所研究的任务RNN和神经动力学（如类似ramping activity的跨区域活动模式）具有重要参考价值。

---

### 10. 📌 The cost of efficiency in flexible neural representations (2026 May)
- 灵活神经表征中效率的代价
- **Author and Affiliation**: Dang, W. (Vanderbilt University); Corresponding Author: Christos Constantinidis (Vanderbilt University)
- **Journal**: BioRxiv (预印本)
- **Link/DOI**: https://doi.org/10.64898/2026.05.18.722885
- **Target Audience**: Zixiang
- **Figures to Locate**: 摘要未明确图号，根据内容推测相关结果展示至少包括：神经子空间重叠分析图（neural subspace overlap）、行为正确率与子空间重叠的关系图、模型RNN的动力学对比图、以及胆碱能刺激前后的效果图。

#### 📊 Overview
- **Motivation & Goal**: 工作记忆（working memory）依赖于神经活动对刺激信息的灵活表征（flexible representation），这种表征会随任务需求动态变化。过去观点认为，刺激表征的转换（transformation）是高效使用神经资源且对任务执行最优的。然而，这些转换背后的神经机制往往不透明，且效率（efficiency）可能与最优性能（optimal performance）存在冲突。本文旨在研究这种冲突：当需要在工作记忆中根据情境线索选择性回忆两个刺激之一时，前额叶皮层（prefrontal cortex）的神经表征究竟是如何组织的，效率与正确性之间是否存在根本性的权衡（tradeoff）。动机源于对“表征的效率是否总是有益”这一假设的挑战，并试图揭示其潜在的神经成本。

- **Methodology**: 实验采用两个雄性猴子执行一个工作记忆任务（working memory task），任务要求根据一个情境线索（context cue）选择性回忆两个刺激中的一个。主要记录前额叶皮层（prefrontal cortex）的神经活动。数据分析采用子空间分析（subspace analysis）方法，探究神经活动在高维空间中的组织方式，特别是区分“共享子空间”（shared neural subspace）与“不同子空间”（distinct subspaces）的假设。同时，作者训练了循环神经网络（recurrent neural networks, RNNs）来模拟相同的任务，以验证神经表征的效率-效果权衡是否在模型中也成立。此外，还进行了胆碱能前脑刺激（stimulation of the cholinergic forebrain）实验，观察其对行为表现和神经表征结构的影响。核心是通过比较不同子空间重叠程度与行为错误率的关系，量化“效率代价”。

- **Key Results**: 主要发现包括：
  1. **效率优先的默认机制**：在任务中，前额叶皮层优先采用效率模式——即通过在一个共享神经子空间内“覆写（overwriting）”信息来编码两个刺激，而不是为每个刺激维持不同的子空间（distinct subspaces）。这种共享子空间的使用使表征更“高效”（占用更少神经维度）。
  2. **效率的代价**：无论是真实的神经数据还是训练的RNN模型，更加高效（子空间重叠越大）的表征往往伴随着更高的行为错误率。即效率牺牲了有效性（effectiveness），表现为更易出错。
  3. **胆碱能刺激改变默认机制**：对胆碱能前脑（cholinergic forebrain）进行电刺激可以改善猴子的行为表现，并且这种刺激改变了默认的编码方式——使得不同情境（context）被编码在更高的维度（higher dimensions）中，即维持了更分离的子空间，从而降低了效率-效果的冲突。

- **Conclusion**: 本工作揭示了在灵活更新工作记忆（flexibly updating working memory）时，神经表征的效率与有效性之间存在一个根本性的权衡（fundamental tradeoff）。默认情况下，神经系统倾向于通过共享子空间覆写信息来实现高效编码，但这会带来错误率的上升。通过外部刺激（如胆碱能调制）可以改变这种默认策略，以牺牲一定效率换取更高的准确性。这一发现挑战了“高效表征总是最优”的传统观点，并指出了神经资源利用与任务性能之间的平衡点。

- **Innovation & Implications**: 真正的创新在于：首次明确量化并证明了神经表征的“效率代价”（cost of efficiency），并展示了在任务执行RNN模型中这一权衡也成立。这对Zixiang的研究兴趣有直接且重要的启示：（1）为task-performing RNN的设计提供了新约束——不能只追求表征的低维高效，必须考虑模型在认知任务中的错误率与子空间重叠的关联；（2）对工作记忆的recurrent models建模时，可以引入“子空间重叠度”作为可调参数，检验效率与准确度的关系；（3）胆碱能刺激的结果提示，生物体中存在可调节这种权衡的神经调制机制（neuromodulation），未来可在RNN中引入类似调制因子模拟灵活性变化。此外，该方法学（神经子空间分析和RNN对比）对全实验室研究神经网络动力学的low-dimensional dynamics和connectivity motifs也具参考价值。

---

### 11. 📌 A context-free model of savings in motor learning (2026 Jan/Feb)
- 运动学习中无情境提示的“节省”现象的模型
- **Author and Affiliation**: Paul L Gribble, Western University (affiliations from RSS feed)
- **Journal**: eLife
- **Link/DOI**: https://elifesciences.org/articles/107423
- **Target Audience**: Whole lab
- **Figures to Locate**: Figures demonstrating the behavioral savings effect (e.g., force profiles across NF1/FF1/NF2/FF2), the dependence of savings on RNN unit number, and the identification & perturbation of preparatory activity shifts.

#### 📊 Overview
- **Motivation & Goal**: 在运动学习中，“节省”（savings）指的是第二次暴露于同一扰动时，学习速度比第一次更快。尽管已有大量研究，其神经机制仍然争议很大。最近有观点认为，神经控制的高维度特性允许学习痕迹在干扰后得以留存，从而促进后续的再学习。该论文旨在通过训练的循环神经网络（RNN）控制上肢生物力学模型，检验这一假设，并探究是否不需要任何情境提示（如施加扰动的背景信号）就能复现节省行为，以及网络规模与神经活动模式如何参与其中。研究期望揭示节省现象不依赖于认知或策略性学习，而是源于高维神经回路的内在记忆保留特性。
- **Methodology**: 该研究使用了开源的 MotorNet 框架，训练 RNN 来控制一个生物力学模型的人上肢。训练任务是让 RNN 控制模型进行水平面的触达运动，训练序列包含：NF1（无扰动的基线）、FF1（施加速度依赖力场的适应阶段）、NF2（去除力场的清洗阶段）、FF2（再次施加同一力场的再适应阶段）。RNN 的输入包括关节角度、关节速度以及运动目标位置，输出为肌肉激活信号；没有给网络提供任何感知或情境提示来表示力场是否存在。通过比较再适应（FF2）与初始适应（FF1）的运动偏差（如力补偿等），量化 savings。此外，作者系统改变了 RNN 的隐藏层单元数量（从50到500不等）来观察网络维度对 savings 的影响。通过降维方法和扰动实验，分析 RNN 内部的神经活动成分，特别是准备活动（preparatory activity）在运动开始前的状态偏移，并直接操纵该偏移以检验其对 savings 的因果作用。
- **Key Results**: (1) RNN 在没有任何情境提示的情况下，表现出了典型的行为节省：在再适应阶段（FF2）比初始适应（FF1）更快地恢复准确运动，部分网络在清洗阶段（NF2）后仍保留有利于快速再适应的活动痕迹。(2) 节省的强度与网络规模正相关：具有更多隐藏单元的网络表现出更显著的 savings，表明高维度有利于记忆保留。(3) 通过分析神经活动，作者发现了一个与 savings 相关的成分——在清洗阶段结束后，网络的准备活动（运动开始前的活动状态）相对于基线出现了持久的偏移，该偏移方向与初始适应后发生的变化同向。 (4) 因果干扰实验证实：在再适应前人为地在准备活动朝向该偏移的方向上进行调整，能增强 savings；反之如果反向调整，则削弱甚至消除 savings。这建立了该神经活动变化与行为 savings 的直接联系。
- **Conclusion**: 该工作通过一个控制生物力学模型的 RNN 框架，证明 savings 可以在完全无情境提示的条件下从神经回路的内在动力学自发出，且依赖于网络的高维度特性。准备活动的持久偏移是这一现象的关键神经基础。这一结果支持了运动记忆中 savings 可能源于神经控制的高维度和对运动记忆痕迹的隐式保留，而非依赖于 explicit 的策略或情境认知。该模型为理解运动学习中记忆的维持与再利用提供了具体的计算机制和可检验的神经预测。
- **Innovation & Implications**: 本文最大的创新在于两个方面：(1) **纯内在机制的展示**：将 savings 归因于高维神经回路在训练中形成的内源活动重构，而不需要任何外部情境提示或高级认知介入，这在以往的实验或模型中很少被如此干净地验证。(2) **因果验证**：直接通过扰动准备活动来增强或消除 savings，而不仅仅是相关性分析，使得机制的结论更加可靠。对于整个实验室而言，该工作直接关联到我们“神经网络动力学与维度”的核心兴趣：它系统地探索了网络大小（即维度）如何影响动力学的持久性或记忆特性，并且精确刻画了准备活动作为一种低维慢动态如何编码并影响后续行为。此外，该方法提供了分析 RNN 隐动态的有效范式：识别时间上的特定活动子空间（如准备活动）并对其进行因果性操作。这为我们研究其他认知任务（如工作记忆、决策）中的神经动力学痕迹提供了一个很有价值的工具和思考框架。

---

### 12. 📌 Modeling flexible behavior with remapping-based hippocampal sequence learning (2025)
- 基于重映射的海马序列学习建模灵活行为
- **Author and Affiliation**: Yoshiki Ito, National Institute for Physiological Sciences (NIPS)
- **Journal**: eLife
- **Link/DOI**: https://elifesciences.org/articles/106506
- **Target Audience**: Zhanmiao
- **Figures to Locate**: 由于全文未提供，需关注模型架构（Context selector 与 hippocampus 序列生成模块）、不同上下文下的 neural activity（remapping 现象）、以及 optogenetic inactivation 和 clinical 模拟的相关结果图。

#### 📊 Overview
- **Motivation & Goal**: 动物可以根据上下文（context）灵活切换行为，海马（hippocampus）被认为是这一过程的关键脑区，其神经活动表现出上下文依赖的序列活动（context-dependent sequential activity）。然而，这种序列活动如何通过神经元活动重组（remapping）来建立，及其如何支持灵活行为，尚不明确。本文旨在提出一个生物合理的强化学习模型，用于解释海马序列活动的形成机制，并说明其如何贡献于上下文依赖的灵活行为切换。
- **Methodology**: 作者提出了一个**生物合理的强化学习模型（biologically plausible reinforcement learning model）**，其中包含一个**Context selector**模块（负责根据当前上下文选择不同的海马活动模式）。该模型模拟了海马序列活动的形成过程：通过 remapping（神经元活动重映射）实现上下文间的活动分离；使用 eligibility trace 等机制实现学习，避免对 backpropagation 的依赖。模型在多个任务场景中进行了验证，并复现了多种实验数据：包括神经活动记录、光遗传失活（optogenetic inactivation）效应、人类功能磁共振成像（fMRI）结果以及临床研究中的行为异常。
- **Key Results**:
  1. 模型成功复现了海马在不同上下文下的**remapping**现象，即一组神经元在一类上下文中活跃而在另一类中沉默。
  2. **Context selector** 使得模型能在多个任务之间灵活切换，无需重新训练整体网络。
  3. 模拟**光遗传失活**实验：抑制 Context selector 会破坏上下文依赖的行为切换，导致序列活动混乱。
  4. 模型还能解释人类 fMRI 中 seen 的海马前-后轴（anterior-posterior）功能差异。
  5. 模型预测：如果 Context selector 中**感觉表征（sensory representation）** 与**上下文表征（contextual representation）**的比例失衡，则会导致类似**精神分裂症（schizophrenia）** 和**自闭症谱系障碍（autism spectrum disorder）** 的行为——例如对上下文无法正确识别或过度泛化。
- **Conclusion**: 本文提出的基于 remapping 的海马序列学习模型，以生物合理的强化学习框架解释了上下文依赖的灵活行为背后的神经机制。模型不仅复现了多层次实验观察，还作出了可检验的临床相关预测，为理解海马在灵活行为中的作用及其紊乱提供了计算基础。
- **Innovation & Implications**: 本文的创新点在于将**remapping**与**生物合理强化学习**有机结合，提出了一个完整、可模拟多种实验范式的计算框架。对于本实验室（尤其是 Zhanmiao 关注生物合理学习和替代反向传播的算法），此模型展示了如何使用 eligibility trace 和 context selector 实现灵活的序列行为学习，且没有依赖误差反向传播。该工作也为理解海马动力学（如序列活动的形成）提供了理论工具，可用于指导未来对皮层-海马环路中 working memory 与 context-dependent  dynamics 的研究。

---

### 13. 📌 Distinct activity in prefrontal projections promotes temporal control of action (2025 May)
- 前额叶投射中的不同活动促进动作的时间控制
- **Author and Affiliation**: Xin Ding (Department of Neurology, University of Iowa), Corresponding Author(s): Nandakumar S. Narayanan (Department of Neurology, University of Iowa; Iowa Neuroscience Institute)
- **Journal**: PNAS
- **Link/DOI**: https://www.pnas.org/doi/abs/10.1073/pnas.2538059123
- **Target Audience**: Zixiang
- **Figures to Locate**: Figure 2 for ramping patterns (PFC整体ramping活动), Figure 3 for PFC-MD和PFC-DMS的fiber photometry ramping up/down对比, Figure 4 for 失活实验对时间估计的影响

#### 📊 Overview
- **Motivation & Goal**: 前额叶皮层（PFC）神经元在执行认知功能（如工作记忆、注意力、计时）时表现出多样化的活动模式，但这种异质性如何与解剖连接相关联尚不清楚。本文旨在通过解剖连接（anatomical connectivity）的角度理解PFC活动的多样性。作者利用回路特异性工具（circuit-specific tools）在小鼠间隔计时任务（interval timing）中记录不同PFC投射的活动。间隔计时是一个高度可转化的认知过程，需要工作记忆来维持时间规则，并需要注意力关注时间的流逝以估计几秒的时间间隔。核心目标是揭示PFC投射到内侧丘脑（MD）和背内侧纹状体（DMS）的神经元在时间控制中扮演的不同角色。
- **Methodology**: 实验采用小鼠进行间隔计时任务（固定间隔杠杆按压任务，要求动物等待几秒后做出反应）。首先使用神经元记录（neuronal recordings）捕获PFC整体在间隔计时中的活动，发现主要模式为单调的时间依赖性ramping（斜坡活动）。随后利用逆行病毒（retrograde viruses）分别标记PFC投射到MD（PFC-MD）和PFC投射到DMS（PFC-DMS）的神经元，并通过光纤光度测定（fiber photometry）记录这两类投射在计时任务中的钙信号动态。接着进行回路特异性失活（circuit-specific inactivation，使用光遗传学抑制PFC-DMS投射），观察动物时间估计行为的变化。最后对投射定义的神经元进行单核RNA测序（single-nucleus RNA sequencing），比较PFC-MD和PFC-DMS神经元的转录组轮廓（transcriptomic profiles），寻找与连接特异性和功能差异相关的基因。
- **Key Results**: 主要发现有三点。第一，光纤光度记录显示，PFC-MD和PFC-DMS投射在间隔计时过程中编码不同的时间信号：PFC-MD投射的钙信号在时间间隔内呈向下ramping（ramping down，接近反应时间时活动降低），而PFC-DMS投射则呈向上ramping（ramping up，接近反应时间时活动升高）。第二，回路特异性失活实验表明，抑制PFC-DMS投射会破坏动物对时间的内在估计（internal estimates of time），导致反应时间变异性增大或精度下降。第三，单核RNA测序揭示了两类投射神经元具有不同的转录组特征，富集了皮层分层相关基因（如Cux2、Camk2n1、Htr4、Foxp2等），表明基因表达差异与连接特异性和活动模式相关。
- **Conclusion**: 这些数据表明，PFC至不同下游脑区的投射在间隔计时中表现出相反的ramping活动模式（向下 vs 向上），且PFC-DMS投射对时间估计行为至关重要。此外，投射特异性神经元的转录组差异为理解前额叶功能异质性的分子基础提供了线索。这些发现推进了对前额叶功能以及人类疾病中前额叶功能障碍的基本理解。
- **Innovation & Implications**: 本文的创新在于结合了回路特异性记录、行为操纵和转录组分析，系统地将PFC的时间相关ramping活动与特定的解剖投射路径联系起来。对于Zixiang的课题而言，该实验直接提供了两个投射（PFC-MD向下ramping、PFC-DMS向上ramping）在间隔计时任务中的精确动态模式，这是构建任务执行型RNN（task-performing RNN）或工作记忆模型时非常宝贵的实验约束（experimental constraints）和验证数据。这些明确的ramping方向差异可以作为模型训练的目标模式，帮助理解不同下游通路如何协同产生精确的时间控制。此外，论文中使用的纤维光度记录和行为范式也为小鼠实验中的神经动力学采集提供了参考。虽然本文未涉及计算模型，但其发现的ramping dynamics对Zixiang关注的认知任务中的神经动力学（ramping activity）以及有效连接推断（不同投射的连接特异性）具有直接的应用价值。
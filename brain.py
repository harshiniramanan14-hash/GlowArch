from agents import GlowAgents

def process_glow_query(user_profile, query, active_modes):
    """
    Orchestrates the multi-agent system based on user-selected modalities.
    """
    expert_outputs = {}
    
    # Run selected expert agents
    if "Skincare Expert" in active_modes:
        agent = GlowAgents.get_skincare_expert(user_profile, query)
        expert_outputs["Skincare"] = agent.invoke({"user_profile": user_profile, "query": query}).content

    if "Cosmetic Chemist" in active_modes:
        agent = GlowAgents.get_cosmetic_expert(user_profile, query)
        expert_outputs["Cosmetics"] = agent.invoke({"user_profile": user_profile, "query": query}).content

    if "Natural Remedies" in active_modes:
        agent = GlowAgents.get_home_remedy_expert(user_profile, query)
        expert_outputs["Home Remedies"] = agent.invoke({"user_profile": user_profile, "query": query}).content

    if "Facial Fitness" in active_modes:
        agent = GlowAgents.get_exercise_expert(user_profile, query)
        expert_outputs["Exercises"] = agent.invoke({"user_profile": user_profile, "query": query}).content

    # Synthesize answers using the general GenAI Brain if multiple experts are active
    if len(expert_outputs) > 1:
        combined_text = "\n\n".join([f"### {k} Agent:\n{v}" for k, v in expert_outputs.items()])
        brain = GlowAgents.get_general_brain()
        summary = brain.invoke({"expert_responses": combined_text}).content
        expert_outputs["Master Synthesis Roadmap"] = summary

    if not expert_outputs:
    expert_outputs["Error"] = (
        "No expert responses were generated. "
        "Please check the selected experts and your API configuration."
    )

return expert_outputs


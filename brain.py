from agents import GlowAgents


def process_glow_query(user_profile, query, active_modes):
    """
    Runs selected expert agents and optionally synthesizes
    the responses into one final roadmap.
    """

    expert_outputs = {}

    try:

        if "Skincare Expert" in active_modes:
            agent = GlowAgents.get_skincare_expert(user_profile, query)
            expert_outputs["🧴 Skincare Expert"] = (
                agent.invoke(
                    {
                        "user_profile": user_profile,
                        "query": query,
                    }
                ).content
            )

        if "Cosmetic Chemist" in active_modes:
            agent = GlowAgents.get_cosmetic_expert(user_profile, query)
            expert_outputs["🧪 Cosmetic Chemist"] = (
                agent.invoke(
                    {
                        "user_profile": user_profile,
                        "query": query,
                    }
                ).content
            )

        if "Natural Remedies" in active_modes:
            agent = GlowAgents.get_home_remedy_expert(user_profile, query)
            expert_outputs["🌿 Natural Remedies"] = (
                agent.invoke(
                    {
                        "user_profile": user_profile,
                        "query": query,
                    }
                ).content
            )

        if "Facial Fitness" in active_modes:
            agent = GlowAgents.get_exercise_expert(user_profile, query)
            expert_outputs["💆 Facial Fitness"] = (
                agent.invoke(
                    {
                        "user_profile": user_profile,
                        "query": query,
                    }
                ).content
            )

        if len(expert_outputs) > 1:

            combined = "\n\n".join(
                f"{k}\n{v}"
                for k, v in expert_outputs.items()
            )

            brain = GlowAgents.get_general_brain()

            expert_outputs["✨ Master Glow Roadmap"] = (
                brain.invoke(
                    {
                        "expert_responses": combined
                    }
                ).content
            )

    except Exception as e:

        expert_outputs["❌ Error"] = str(e)

    if not expert_outputs:

        expert_outputs["⚠️ No Response"] = (
            "No expert generated a response."
        )

    return expert_outputs

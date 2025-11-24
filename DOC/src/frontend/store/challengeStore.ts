import { create } from "zustand"

interface Challenge {
  id: number
  title: string
  coins_reward: number
  created_at: string
  description: string
  instructions: string
}

interface ChallengeStore {
  selectedChallenge: Challenge | null
  setSelectedChallenge: (challenge: Challenge) => void
  clearSelectedChallenge: () => void
}

export const useChallengeStore = create<ChallengeStore>((set) => ({
  selectedChallenge: null,
  setSelectedChallenge: (challenge) => set({ selectedChallenge: challenge }),
  clearSelectedChallenge: () => set({ selectedChallenge: null }),
}))

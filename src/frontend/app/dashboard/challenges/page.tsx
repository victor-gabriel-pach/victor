"use client"

import { useQuery } from "@tanstack/react-query"
import { getChallenges } from "@/lib/api"
import { useChallengeStore } from "@/store/challengeStore"
import { useRouter } from "next/navigation"
import ChallengeCard from "@/components/common/ChallengeCard"

export default function ChallengesPage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["challenges"],
    queryFn: getChallenges,
  })

  const { setSelectedChallenge } = useChallengeStore()
  const router = useRouter()

  if (isLoading) return <p>Carregando desafios...</p>
  if (error) return <p>Erro ao carregar desafios 😢</p>

  const challenges = data?.results || data || []

  return (
    <section className="px-4 py-4">
      <h1 className="text-4xl font-black mb-8">Desafios</h1>
      <div className="grid grid-cols-4 gap-4">
        {challenges.map((c: any) => (
          <div
            key={c.id}
            onClick={() => {
              setSelectedChallenge(c)
              router.push(`/dashboard/challenges/${c.id}`)
            }}
          >
            <ChallengeCard
              title={c.title}
              coinsReward={c.coins_reward}
              createdAt={new Date(c.created_at)}
            />
          </div>
        ))}
      </div>
    </section>
  )
}

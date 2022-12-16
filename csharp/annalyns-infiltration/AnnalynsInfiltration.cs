using System;

static class QuestLogic
{
    public static bool CanFastAttack(bool knightIsAwake)
    {
        if (knightIsAwake == false) { return true; }
        return false;
   
    }

    public static bool CanSpy(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake)
    {
        if(knightIsAwake== true || archerIsAwake == true || prisonerIsAwake == true) { return true; }
        return false;
    }

    public static bool CanSignalPrisoner(bool archerIsAwake, bool prisonerIsAwake)
    {
        if(prisonerIsAwake==true && archerIsAwake== false) { return true; }
        return false;
    }

    public static bool CanFreePrisoner(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake, bool petDogIsPresent)
    {
        if(knightIsAwake==false && archerIsAwake==false && prisonerIsAwake == false)
        {
            if(petDogIsPresent == true) { return true; }
        }
        if(knightIsAwake==true && archerIsAwake == false && prisonerIsAwake == true)
        {
            if (petDogIsPresent == true) { return true; }
        }

        if(knightIsAwake==true &&archerIsAwake==false && prisonerIsAwake == false)
        {
            if(petDogIsPresent == true) { return true; }
        }

        if(knightIsAwake==false && archerIsAwake == false && prisonerIsAwake == true)
        {
            return true;
        }
        return false;
    }
}

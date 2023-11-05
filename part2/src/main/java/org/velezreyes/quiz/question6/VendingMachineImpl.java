package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

    private int insertedMoney = 0;
    private Map<String, Drink> drinkInventory;

    public VendingMachineImpl() {
        this.drinkInventory = new HashMap<>();
        // Add available drinks and their prices to the inventory
        drinkInventory.put("ScottCola", new DrinkImpl("ScottCola", 75, true));
        drinkInventory.put("KarenTea", new DrinkImpl("KarenTea", 100, false));
    }

    @Override
    public void insertQuarter() {
        insertedMoney += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
      Drink selectedDrink = drinkInventory.get(name);

      if (selectedDrink == null) {
        throw new UnknownDrinkException();
      }

      if (insertedMoney >= selectedDrink.getPrice()) {
        insertedMoney -= selectedDrink.getPrice();
        return selectedDrink;
      } else {
        throw new NotEnoughMoneyException();
      }
    }
    
    public static VendingMachine getInstance() {
      return new VendingMachineImpl();
  }
    
}

package org.velezreyes.quiz.question6;

public class DrinkImpl implements Drink {
    private String name;
    private int price;
    private boolean isFizzy;

    public DrinkImpl(String name, int price, boolean isFizzy) {
        this.name = name;
        this.price = price;
        this.isFizzy = isFizzy;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return isFizzy;
    }

    @Override
    public int getPrice() {
        return price;
    }
}
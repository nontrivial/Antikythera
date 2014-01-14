package antikythera.time;

/**
 * Created by Nick on 1/14/14.
 */
public abstract class TimeUnit {
    public abstract void setHolidays(Calendar holiday);
    public abstract boolean isBefore(TimeUnit t);
    public abstract boolean isAfter(TimeUnit t);
    public abstract TimeUnit minus(TimeUnit t);
    public abstract TimeUnit plus(TimeUnit t);

    public abstract DayOfWeek getDayOfWeek();
    public abstract int getDayOfMonth();
    public abstract int getMonth();
    public abstract int getYear();

    public abstract void parseFrom(String t);

    public abstract boolean isWithin(TimeUnit t1, TimeUnit t2);

    public enum DayOfWeek {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday}
/*
fetch all prices between 2:30 to 3:30 each day from 20110101 to 20130101 excluding holidays and Thursdays
 */
}

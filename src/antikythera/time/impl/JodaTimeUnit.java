package antikythera.time.impl;

import antikythera.time.Calendar;
import antikythera.time.TimeUnit;
import org.joda.time.DateTime;

/**
 * Created by Nick on 1/14/14.
 */
public class JodaTimeUnit extends TimeUnit {

    private DateTime time;

    public JodaTimeUnit(DateTime time) {
        this.time = time;
    }

    @Override
    public void setHolidays(Calendar holiday) {

    }

    @Override
    public boolean isBefore(TimeUnit t) {
        return false;
    }

    @Override
    public boolean isAfter(TimeUnit t) {
        return false;
    }

    @Override
    public TimeUnit minus(TimeUnit t) {
        return null;
    }

    @Override
    public TimeUnit plus(TimeUnit t) {
        return null;
    }

    @Override
    public DayOfWeek getDayOfWeek() {
        return null;
    }

    @Override
    public int getDayOfMonth() {
        return 0;
    }

    @Override
    public int getMonth() {
        return 0;
    }

    @Override
    public int getYear() {
        return 0;
    }

    @Override
    public void parseFrom(String t) {

    }

    @Override
    public boolean isWithin(TimeUnit t1, TimeUnit t2) {
        return false;
    }
}

